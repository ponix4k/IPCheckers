#!/usr/bin/python3
import os
import sys
from datetime import datetime

sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
path ="ips"
Last_IP = 'ips/lastip.txt'
Current_IP = 'ips/currentip.txt'
Same_IP = False

def Last_IP_Check():
    if os.path.isfile(Last_IP):
        print("Last IP [OK]")
    else:
        print("Last IP [ERROR]")
        if not os.path.exists(path):
            os.mkdir(path)
            print ("Path has been created")
        f1 = open(Last_IP,'w')
        f1.write ('0.0.0.0')
        f1.close
        print("Last IP [CREATED]")

def Current_IP_Check():
    if os.path.isfile(Current_IP):
        print("Current IP [OK]")
    else:
        print("Current IP [ERROR]")
        f2 = open(Current_IP,'w')
        f2.write ('0.0.0.0')
        f2.close
        print("Current IP [CREATED]")


def Get_Current_IP():
    l1 = open('log.txt','a+')
    print ('Getting Current...')
    GetCurrentIP = os.popen('curl ifconfig.me')
    CIP = GetCurrentIP.read()
    l1.write(sttime+' <INFO> '+' Checking Current IP \n')
    f2 = open(Current_IP,'w')
    f2.write (CIP)
    f2.close
#    print('Current IP is: '+ CIP)

def Main():
    Last_IP_Check()
    Current_IP_Check()
    f1 = open(Current_IP,'r')
    CIP = f1.read()
    f2 = open(Last_IP,'r')
    LIP = f2.read()
    Same_IP = False
    print ('Current ip is: '+ CIP)
    print ('Last IP was: '+ LIP)
    if CIP == LIP:
        Same_IP == True
        #print ("IP is the same")
        print ('No Changes')
        l1 = open('log.txt','a+')
        l1.write(sttime+' <INFO> -'+' IP is unchanged'+'\n')
    else:
        Same_IP == False
        Print ("IP has changed!")
        l1 = open('log.txt','a+')
        print ('New IP Detected')
        l1.write(sttime+' <INFO> -'+' New IP Detected '+'\n')
        Get_Current_IP()
        l1.write(sttime+' <INFO> -'+' New IP Detected: '+str(Current_IP)+'\n')
        os.system('cp ips/currentip.txt ips/lastip.txt')
        print('IP Address Updated')
        l1.close()
        print ('Emailing new IP')
#        os.system('python3 update_email.py')

Main()

