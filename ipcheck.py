#!/usr/bin/python3
import os
import sys

f1 = open("lastip.txt","r")
last_ip = f1.read()
f1.close()
print (last_ip)

os.system("sh get_currentip.sh")
print ("Checking Current IP")
f2 = open("currentip.txt","r")
current_ip = f2.read()
print (current_ip)
f2.close()

if current_ip == last_ip:
    print ("No Changes")
else:
    print("New IP Detected")
    os.system("sh getip.sh")
    print("IP Address Updated")
    os.system("python3 update_email.py")
