# Script to extract FastQ and MOD informations from FAST5

Fast5 Files must be basecalled with methylation-aware model

"""ModExtract -- Extract FastQ and Modification Results from Fast5 File
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
"""

## Installation:

1) Clone repository
2) Install python requirements
   pip3 install -r requirements.txt
   
   or create virtual environment
