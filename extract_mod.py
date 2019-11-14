"""ModExtract -- Extract FastQ and Modification Results from Fast5 File

Usage:  
    extract_mod.py INPUTDIR
    extract_mod.py  [options] INPUTDIR

Options:
    -h --help               Show this screen
    -o DIR --outDir=DIR     Output directory [default: InputDirectory]
    -a STR --analysis=STR   Select specific basecalling analysis to extracat [default: latest]
    -q --noFastq            Dont extract fastQ files
    -k --keepSkipped        Include Fast5 from the Skipped folder
"""

import os
import h5py
from docopt import docopt
import numpy as np
import pickle

arguments = docopt(__doc__, version='Naval Fate 2.0')

def find_fast5(path = arguments["INPUTDIR"], useFailed = arguments["--keepSkipped"]):
    f5files = []
    # r=root, d=directories, f=files
    for r, d, f in os.walk(path):
        if not(("failed" in str(d)) and useFailed):
            for file in f:
                if '.fast5' in file:
                    f5files.append(os.path.join(r, file))
    return (f5files)

def get_outfile(file, out_type):
    if arguments["--outDir"] == "InputDirectory":
        p = os.path.dirname(file).replace("fast5", out_type)
    else:
        p = os.path(arguments)
     
    os.makedirs(p, exist_ok=True)
    filename = os.path.splitext(os.path.basename(file))[0]
    ext = ".fastq" if out_type == "fastq" else ".mod"

    return(os.path.join(p, filename + ext))

def get_latest_analysis(f5file):
    if  arguments["--analysis"] == "latest":
        read1 = next(iter(f5file.keys()))
        analyses = list(f5file[read1].get("Analyses").keys())
        latest = sorted([x for x in analyses if "Basecall" in x])[-1]
        print("Latest analysis found:", latest)
        return(latest)
    else:
        return(arguments["--analysis"])

def extract_data (file):
    f = h5py.File(file, 'r')
    analysis = get_latest_analysis(f)
    file_fq = (get_outfile(file, "fastq"))
    file_mod = (get_outfile(file, "mod"))
    
    # Remove existing files to overwrite them later
    try:
        print("Removing existing files")
        os.remove(file_fq)
        os.remove(file_mod)
    except:
        pass

    mods = {"fast5name":file, "mod_values":{}}

    for read in list(f.keys())[1:10]:
        #print("Read: ", read)
    
        if not (arguments["--noFastq"]): 
            # Write Fastq
            fastq = f[read].get("Analyses/" + analysis + "/BaseCalled_template/Fastq")
            if os.path.exists(file_fq):
                append_write = 'a'
            else:
                append_write = 'w'
            outfq = open(file_fq, append_write)
            outfq.write(fastq[()].decode())
            outfq.close

        # Extract mod values and add to library
        mods["mod_values"][read] = f[read].get("Analyses/"+ analysis + "/BaseCalled_template/ModBaseProbs")[()]

    #print("saving modfile to ", file_mod)
    pickle.dump(mods, open(file_mod, "wb"))

## Start main Method
files = find_fast5()
print(arguments)
print("Found", len(files), "Fast5 files")
for file in files:
    extract_data(file)    