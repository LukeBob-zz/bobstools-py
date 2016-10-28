#!/usr/bin/python
#
# Author: LukeBob
#
# Run with: nohup python PingBot.py &


import os
import time
from twilio.rest import TwilioRestClient
import sys

ACCSID = 'AC'  # Account SID
AUTHTOK = ''   # Auth Token


while 1:
    time.sleep(20)
    response = os.system('ping -c 1 <Your server> >> /dev/null')
    time.sleep(5)
    if response != 0:
        client = TwilioRestClient(ACCSID, AUTHTOK)
        client.messages.create( body="Server is Down", to="<Mobile number>", from_="<Twilio Number>")
        time.sleep(10)
        sys.exit(0)
    

