# Script to extract FastQ and MOD informations from FAST5

Fast5 Files must be basecalled with methylation-aware model

```
ModExtract -- Extract FastQ and Modification Results from Fast5 File
Usage:  
    extract_mod.py INPUTDIR
    extract_mod.py  [options] INPUTDIR
Options:
    -h --help               Show this screen
    -t --threads=N          Use N threads [default: 4]
    -o DIR --outDir=DIR     Output directory [default: InputDirectory]
    -a STR --analysis=STR   Select specific basecalling analysis to extracat [default: latest]
    -q --noFastq            Dont extract fastQ files
    -k --keepSkipped        Include Fast5 from the Skipped folder
```

## Installation:

1) Clone repository
2) Install python requirements (or make venv)

    `pip3 install -r requirements.txt`

## Output:

This script produces:

- `Gzip` compressed FastQs
- Modification informations. The files are gzipped and pickled python libraries. To load the data into python for further analysis use the following code:

 ```
 import pickle
 import gzip
 
 dat = pickle.load(gzip.open("myread.mod.gz", "rb"))
 ```
 
 This data is pretty useless on its own, a consensus module based on a minimap alignment might be really useful...
