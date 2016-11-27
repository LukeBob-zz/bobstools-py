# bobstools-py
experiment kali python gui for making a few tasks simple

## bobstool Setup ##

**just extract the folder and place it anywere on the linux system. Then change python file's permissions;**

* ```chmod +x bobstool.py```
 
**then you can run it with;**

* ```./bobstool.py```

# LogFileCleaner.py 
**Does Exactly what it says on the tin, cleans log dirs.**

## LogFileCleaner setup ##

* ```chmod +x LogFileCleaner.py```

**then edit the script and point it at your log dir, and execute.**

* ```./LogFileCleaner.py```

# EmailScrape.py 
**Pulls down emails from url-list.**

## EmailScrape example ##
**edit the script and insert your url's into the url list like so.**

* ```urlList = ['http://your-url.com','https://your-url2.com']```

**then run with**

* ``` ./EmailScrape.py```

# Win-Pwn

**Multicast Ipv6 Packets to all nodes on the network making them join over a thousand new fake addresses. Serverly Affects Windows-7 machines and earlier, running their cpu usage upto 100% and will sit at that usage for sometimes hours, making the device unresponsive**

**Warning Do NOT use on any network that hasnt been setup specifically for testing purposes**

**Run With**

    $ python Win-pwn.py
    
    
    ./Win-pwn.py 

                  _
                 (_)
        __      ___ _ __      _ ____      ___ __
        \ \ /\ / | | '_ \    | '_ \ \ /\ / | '_ \
         \ V  V /| | | | |   | |_) \ V  V /| | | |
          \_/\_/ |_|_| |_|   | .__/ \_/\_/ |_| |_|
                             | |
                             |_|         

          Breaking all windows now...

# Bob-Dir

**Bob dir, http directory bruteforcer written in python needs a wordlist and a host**

**To run**

    $ python Bob-Dir.py 
    
    
          #########################################################
          #                                                       #
          #                   Bob's Directory Buster              #
          #                                                       #
          #########################################################


     Wordlist: 


     ==================================================================================
      Usage:  wordlist: /usr/share/wordlists/dirbuster/directory-list-1.0.txt
      Host: localhost  |  http://localhost.co.uk
     ==================================================================================
     
     $

