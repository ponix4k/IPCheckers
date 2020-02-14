#!/usr/bin/python3
import os
import sys
from datetime import datetime
f1 = open('ips/lastip.txt','r')
l1 = open('log.txt','a+')
last_ip = f1.read()
sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
print (last_ip)

os.system('sh get_currentip.sh')
print ('Checking Current IP')
l1.write(sttime+' <INFO> '+' Checking Current IP \n')
f2 = open('ips/currentip.txt','r')
current_ip = f2.read()
print (current_ip)


if current_ip == last_ip:
    print ('No Changes')
    l1.write(sttime+' <INFO> -'+' No Charges to ip: '+str(last_ip)+'\n')
else:
    print('New IP Detected')
    l1.write(sttime+' <INFO> -'+' New IP Detected '+'\n')
    os.system('sh getcurrent_ip.sh')
    l1.write(sttime+' <INFO> -'+' New IP Detected: '+str(current_ip)+'\n')
    os.system('cp ips/currentip.txt ips/lastip.txt')
    print('IP Address Updated')
    l1.write(sttime+' <INFO> -'+' IP Address Updated'+'\n')
    l1.close()
    f1.close()
    f2.close()
    os.system('python3 update_email.py')
