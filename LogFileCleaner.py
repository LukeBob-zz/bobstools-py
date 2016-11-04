#!/usr/bin/python
#
# Author LukeBob
#
# Clears all files it finds that you specify.

import os.path
import glob, os, sys
import subprocess
import time

split = '==========================================='
logDir = '/var/log/*.gz' # Log directory, you can use globing ie, *.txt


def remove(infile):
    subprocess.call('rm '+infile, shell=True)
    

def main():
    count = 0
    if glob.glob(logDir):
        print split
        print '  Cleaning: '+logDir
        print split+'\n'
    else:
        print split
        print '  No files found in Dir:  '+logDir
        print split
        sys.exit(0)

    for gzFile in sorted(glob.glob('/var/log/*.gz')):
        print "Removing: " + gzFile
        time.sleep(0.5)
        remove(gzFile)
        count = count+1
    print '\n'
    print split
    print ' All Files Removed!  '+str(count)
    print split
    sys.exit(0)    
        
if __name__ == '__main__':
    main()
