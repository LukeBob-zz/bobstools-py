#!/usr/bin/python

########################################################
#            Author: LukeBob                           #
#                                                      #
#       Simple Directory Brute-Forcer                  #
#                                                      #
########################################################

from datetime import datetime
import requests
import time
import sys, traceback
import os
import time
import subprocess
import threading
from threading import Thread

class colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKBLUE = '\033[94m'

list1 = []
list2 = []
MAX_THREADS = 20
subprocess.call('clear', shell=True)
smallSplit = colors.BOLD + colors.OKBLUE + '============================' + colors.ENDC
split = colors.BOLD + colors.OKBLUE + '==================================================================================' + colors.ENDC
start = colors.OKGREEN + colors.BOLD + '''          #########################################################
          #                                                       #
          #                   Bob's Directory Buster              #
          #                                                       #
          #########################################################''' + colors.ENDC               
print '\n'
print start

try:
    def usage():
        print '\n'
        print split
        print colors.BOLD + '''Usage:  wordlist: /usr/share/wordlists/dirbuster/directory-list-1.0.txt
        Host: google.com  |  http://www.google.com''' + colors.ENDC
        print split
        print '\n'
        sys.exit(0)

    print '\n'
    files = raw_input(colors.BOLD + 'Wordlist: ' + colors.ENDC)
    if files == "":
        usage()
    else:
        check1 = os.path.exists(files)

    if check1 == False:
       print '\n'
       print split
       print colors.BOLD + colors.FAIL + " ERROR:" + colors.ENDC + colors.BOLD + "  Cant find Wordlist: " + files + colors.ENDC
       print split
       print '\n'
       sys.exit(0)
    else:
        print ""
        print colors.BOLD + colors.OKBLUE + "Wordlist", colors.ENDC + colors.BOLD + "==> ", colors.BOLD + colors.OKGREEN + files + colors.ENDC
        print '\n'
        host = str(raw_input(colors.BOLD + "Host: " + colors.ENDC))
        if host == "":
            usage()
        print ""
        print colors.BOLD + colors.OKBLUE + "Host", colors.ENDC + colors.BOLD + "==> ", colors.OKGREEN + host + colors.ENDC
        print ""
        print split
        print '\n'
        print colors.BOLD + 'Starting the buster..' + colors.ENDC
        numlines = sum(1 for line in open(files))
        half = numlines / 2           
        splitLen = half        
        outputBase = 'output' 

       
        
        input = open(files, 'r').read().split('\n')

        at = 1
        for lines in range(0, len(input), splitLen):
          
            outputData = input[lines:lines+splitLen]

       
          
            output = open(outputBase + str(at) + '.txt', 'w')
            output.write('\n'.join(outputData))
            output.close()

        
            at += 1
       
    if 'http' in host:
        time.sleep(0.01)
        if host.endswith('/') == False:
            host = (host + '/')      
    elif 'http' not in host:
        if host.endswith('/') == False:
            host = ('http://' + host + '/')
        else:
            host = ('http://' + host)

    subprocess.call('clear', shell=True)
    print "\n"
    print colors.BOLD + colors.OKGREEN + '''    #################
    #               #
    #    Busting... #
    #               #
    #################''' + colors.ENDC
    print '\n'
    print smallSplit
    
    t1 = datetime.now()
    out1 = open('output1.txt')
    out2 = open('output2.txt')
    def thready():
        try:
            for i in out1.readlines():
                r = requests.get(host + i[:-1])
                item = r.status_code
                if item == 200:
                    print '\n'
                    print colors.BOLD + "Directory: " + host + i, "    ==> " + colors.OKGREEN + "Found" + colors.ENDC + colors.BOLD + " 200 Accepted" + colors.ENDC
                    print '\n'
                elif item == 403:
                    print '\n'
                    print colors.BOLD + "Directory: " + host + i, "    ==> " + colors.OKGREEN + "Found" + colors.ENDC + colors.BOLD + " 403 Forbidden" + colors.ENDC
                    print '\n'
                elif item == 401:
                    print '\n'
                    print colors.BOLD + "Directory: " + host + i, "    ==> " + colors.OKGREEN + "Found" + colors.ENDC + colors.BOLD + " 401 Unauthorized" + colors.ENDC
                    print '\n'
                elif item == 429:
                    print '\n'
                    print colors.BOLD + "Directory: " + host + i, "    ==> " + colors.FAIL + "Found" + colors.ENDC + colors.BOLD + " 429 Too Many Requests" + colors.ENDC
                    print '\n'
                    time.sleep(10)
        except KeyboardInterrupt:
            print '\n'
            print smallSplit 
            print colors.BOLD + colors.FAIL + "Shutdown requested...exiting" + colors.ENDC
            print smallSplit
            print '\n'
        except Exception:
            traceback.print_exc(file=sys.stdout)
        sys.exit(0)

    
    def thready2():
        try:
            for i in out2.readlines():
                r = requests.get(host + i[:-1])
                item = r.status_code
                if item == 200:
                    print '\n'
                    print colors.BOLD + "Directory: " + host + i, "    ==> " + colors.OKGREEN + "Found" + colors.ENDC + colors.BOLD + " 200 Accepted" + colors.ENDC
                    print '\n'
                elif item == 403:
                    print '\n'
                    print colors.BOLD + "Directory: " + host + i, "    ==> " + colors.OKGREEN + "Found" + colors.ENDC + colors.BOLD + " 403 Forbidden" + colors.ENDC
                    print '\n'
                elif item == 401:
                    print '\n'
                    print colors.BOLD + "Directory: " + host + i, "    ==> " + colors.OKGREEN + "Found" + colors.ENDC + colors.BOLD + " 401 Unauthorized" + colors.ENDC
                    print '\n'
                elif item == 429:
                    print '\n'
                    print colors.BOLD + "Directory: " + host + i, "    ==> " + colors.FAIL + "Found" + colors.ENDC + colors.BOLD + " 429 Too Many Requests" + colors.ENDC
                    print '\n'
                    time.sleep(10)
        except KeyboardInterrupt:
            print '\n'
            print smallSplit 
            print colors.BOLD + colors.FAIL + "Shutdown requested...exiting" + colors.ENDC
            print smallSplit
            print '\n'
        except Exception:
            traceback.print_exc(file=sys.stdout)
        sys.exit(0)

    while threading.activeCount() < MAX_THREADS:
        try:
            timer = 30
            thread1 = Thread(target = thready)
            thread2 = Thread(target = thready2)
            thread1.start()
            thread2.start()

            
        except KeyboardInterrupt:
            print '\n'
            print smallSplit 
            print colors.BOLD + colors.FAIL + "Shutdown requested...exiting" + colors.ENDC
            print smallSplit
            print '\n'
        except Exception:
            traceback.print_exc(file=sys.stdout)
        sys.exit(0)
   
    t2 = datetime.now()
    total = t2 - t1 
    print "complete in: ", total
    subprocess.call('rm output*.txt', shell=True)
except KeyboardInterrupt:
    print '\n'
    print smallSplit 
    print colors.BOLD + colors.FAIL + "Shutdown requested...exiting" + colors.ENDC
    print smallSplit
    print '\n'
except Exception:
    traceback.print_exc(file=sys.stdout)
sys.exit(0)
   
print "thread finished...exiting"    
  
