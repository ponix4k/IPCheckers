#!/usr/bin/env python3

import os
import sys
import json
import requests
from datetime import datetime

#TODO Get current IP
def get_current_ip():
    r = requests.get("http://ifconfig.me")
    CurrentIP = r.text
    return CurrentIP
    file.write(CurrentIP,)

    print (CurrentIP)

def get_last_ip():
    file=open(last_ip,'r')

#TODO Create log
def create_logs():
    if not os.path.exists(IPPath):
        os.makedirs(IPPath)
        print('Directory Created')
    else:
        if os.path.isfile(IP_log):
            file = open(IP_log, 'r')
            last_IP = file.read()
            print('using existing files')
            return last_IP
        else:
            current_IP = os.popen("curl ifconfig.me").read()
            current_IP = current_IP.strip(' ')
            last_IP = file.write(current_IP)
            print('Creating new files')
            print(last_IP)
            return last_IP
            print(current_IP)
            return current_IP


def get_ts():
    ts = datetime.now().strftime('%Y/%m/%d - %H:%M:%S')
    print(ts)
    return ts

#TODO Read IP Log
def read_iplog():
    file = open(IP_log, 'r')
    last_IP = file.read()
    if last_IP == ('0.0.0.0'):
        file = open(IP_log, 'w')
        current_IP = os.popen("curl ifconfig.me").read()
        current_IP = current_IP.strip(' ')
        file.write(current_IP)
        print('Last IP has been updated ')
        return (last_IP)
    else:
        print('no change')
        return (last_IP)

#TODO Log IP Change
def log_IP_change(old_IP, new_IP):
    with open(log_path, "a+") as log:
        log.write("[{}] <INFO> IP Address Changed! Updating\n".format(
            get_timestamp()))
        log.write("[{}] <INFO> New Address: {}\n\t\t Old Address:{}".format(
            get_timestamp(), new_IP, old_IP))
        with open(IP_log, "w") as iplog:
            iplog.write(new_IP)
            iplog.close()
        log.close()

get_ts()
#get_current_ip()

