#!/usr/bin/python3
#
# Author: LukeBob

import requests
from bs4 import BeautifulSoup
import re
import sys
import time
split = '===================================================='
smlli = '==============='
smll = '====='
urlList = ['http://localhost',] # URL list

class Connect:
    def __init__(self,url):
        self.url = url
        self.request = requests.get(url)

    def run(self):
        soup = BeautifulSoup(self.request.text, 'lxml')
        newSoup =  soup.prettify()
        newsstrip(newSoup)

def newsstrip(text):
    Emails = re.findall(r'[\w.]+@[\w.]+', text)
    if Emails:
        print ('\n')
        for email in Emails:
            print (email)
            time.sleep(0.05)    
    else:
        print ('\nNo Emails Found!..\n')

def main():
    for url in urlList:          
        print (split+'\n'+url+'\n'+split)      
        connection = Connect(url)
        connection.run()
    print ('\n'+smll+'\nDone\n'+smll) 

if __name__ == '__main__':
    main()
