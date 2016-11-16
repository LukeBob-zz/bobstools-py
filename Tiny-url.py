#!/usr/bin/python
#
# Author: LukeBob
#
# Requires pyshortners library.

from pyshorteners import Shortener
import sys
import argparse

split = '==================================='

class url:
    def __init__(self,url):
        self.url = url
        self.shortener = Shortener('Tinyurl')
        
    def Shrink(self): 
        try:   
            return 'New-url: {}'.format(self.shortener.short(self.url))
        except ValueError:
            print '\n Please Enter Valid Url \n'
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='The url you wish to shorten.', type=str)
    args = parser.parse_args()
    
    print '\n         Tiny-url   '
    print ('\n'+split+'\nOld-url: '+(args.url)+'\n'+split)
    
    newurl = (args.url)
    nurl = url(newurl)
    print ('\n'+split+'\n'+nurl.Shrink()+'\n'+split)

if __name__ == '__main__':
    main()
 
