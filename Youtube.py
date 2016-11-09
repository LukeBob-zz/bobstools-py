#!/usr/bin/python3
#
# Author: Luke
#
# List Downloader for use with youtube-dl, made for windows and linux.
# Just Copy and Paste your links into your link.txt and run ./Youtube.py <your-link-file.txt>
# For windows use, Move Youtube.py and your link list to your youtube-dl dir.
# For Linux use, install youtube-dl.

import sys
import os
import subprocess
import time
from pathlib import *

if os.name == 'nt':
    nulll = ' 2>&1>nul'
else:
    nulll = ' >>/dev/null'

def usage():
    print ('\n')
    print ('./Youtube.py <ListOfLinks.txt>')
    print ('\n')
    sys.exit(0)


if len(sys.argv) != 2:
    usage()



def youtubeDl(links):

    print ('\n')
    print ('======================')
    print (' Starting Download... ')
    print ('======================')
    print ('\n')
	
    for link in links:
        subprocess.call('youtube-dl --extract-audio --audio-format mp3 '+(link)+(nulll), shell=True)
        print ('Link: '+(link)+'   Successfully Downloaded.') 
		
    print ('\n')
    print ('======================')
    print (' Download Finished   ')
    print ('======================')
    print ('\n')



   
def main(smallFile):
    if os.path.isfile(smallFile) == False:
        try:
            print ('\n')
            print ('File: '+smallFile+' Not Found!')
            print ('\n')

        except FileNotFoundError:
            print ('File: '+smallFile+' Not Found!')
            print ('\n')
        sys.exit(0)

    if os.path.getsize(smallFile) == 0:
        print('\n')
        print (smallFile, 'File is Empty!')
        print ('\n')
        sys.exit(0)

    list1 = []
    biglist = open(smallFile)

    for link in biglist.readlines():
        if len(link) < 2:
            continue
        list1.append(link[:-1])


    youtubeDl(list1)
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1])
