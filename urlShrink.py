#!/usr/bin/python
#
# Author: LukeBob
# Requires pyshorteners library.

from pyshorteners import Shortener
import sys
import argparse

split = '==================================='
modList = ['tinyurl','isgd','qrcx','osdb']

class url:
    def __init__(self,url,modulee):
        self.url = url
        self.modulee = modulee
        self.shortener = Shortener(self.modulee)
        
    def Shrink(self): 
        try:   
            return 'New-url: {}'.format(self.shortener.short(self.url))
        except ValueError:
            print '\n Please Enter Valid Url \n'
            sys.exit(0)
        except requests.exceptions.ReadTimeout:
            print '\n Problem Connecting to host: '+self.url
            sys.exit(0)

def argList():
    print '\nURL-MODULES\n'
    for modulee in modList:
        print ' '+modulee
    sys.exit(0)

def modules(mod):
    
    if mod not in modList:
        print '\n Module Not Found!\n'
        argList()
    
    if mod == 'osdb':
        return 'Osdb'
    if mod == 'tinyurl':
        return 'Tinyurl'
    elif mod == 'isgd':
        return 'Isgd' 
    elif mod == 'qrcx':
        return 'QrCx'
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', help='The url you wish to shorten.', type=str)
    parser.add_argument('-m','--module', help='Module you wish to use.', type=str)
    parser.add_argument('--module-list', help='List of all current modules.', action="store_true")
    args = parser.parse_args()

    if args.module_list:
        argList()

    if args.module:
        modulee = modules(args.module)
  
        
    print ('\n'+split+'\nOld-url: '+(args.url)+'\n'+split)
    newurl = (args.url)
    nurl = url(newurl,modulee)
    print ('\n'+split+'\n'+nurl.Shrink()+'\n'+split)

if __name__ == '__main__':
    main()
