#!/usr/bin/python

from pyshorteners import Shortener
import sys
import argparse

split = '==================================='
modList = ['tinyurl','isgd','sentala','qrcx','readbility']

class url:
    def __init__(self,url,module):
        self.url = url
        self.module = module
        self.shortener = Shortener(module)
        
    def Shrink(self): 
        try:   
            return 'New-url: {}'.format(self.shortener.short(self.url))
        except ValueError:
            print '\n Please Enter Valid Url \n'
 

def argList():
    print '\nURL-MODULES\n'
    for module in modList:
        print ' '+module
    sys.exit(0)

def modules(mod):
    
    if mod not in modList:
        argList()

    if mod == 'tinyurl':
        return 'Tinyurl'
    elif mod == 'isgd':
        return 'Isgd' 
    elif mod == 'sentala':
        return 'Sentala'
    elif mod == 'qrcx':
        return 'QrCx'
    elif mod == 'readbility':
        return 'Readbility'
    
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url','-u', help='The url you wish to shorten.', type=str)
    parser.add_argument('--module','-m', help='Module you wish to use.', type=str)
    parser.add_argument('--module-list', help='List of all current modules.', action="store_true")
    args = parser.parse_args()

    if args.module_list:
        argList()

    if args.module:
        module = modules(args.module)
        
    print ('\n'+split+'\nOld-url: '+(args.url)+'\n'+split)
    newurl = (args.url)
    nurl = url(newurl,module)
    print ('\n'+split+'\n'+nurl.Shrink()+'\n'+split)

if __name__ == '__main__':
    main()
