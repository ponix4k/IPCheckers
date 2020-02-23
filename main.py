#!/usr/bin/python3
import os
import sys
import smtplib
from datetime import datetime

contact_method_r = open("settings.conf","r")
contact_method = contact_method_r.readlines()[0]
sttime = datetime.now().strftime("%Y%m%d_%H:%M:%S - ")
user = "pi"
path ="/home/"+user+"/IPCheckers"
Last_IP = path + "/ips/lastip.txt"
Current_IP = path + "/ips/currentip.txt"
Same_IP = False

def Last_IP_Check():
    if os.path.isfile(Last_IP):
        print("Last IP [OK]")
    else:
        print("Last IP [ERROR]")
        if not os.path.exists(path):
            os.mkdir(path)
            print ("Path has been created")
        f1 = open(Current_IP,"r")
        LIP = f1.read()
        f2 = open(Last_IP,"w")
        f2.write (LIP)
        f1.close
        f2.close
        print("Last IP [CREATED]")

def Current_IP_Check():
    if os.path.isfile(Current_IP):
        print("Current IP [OK]")
    else:
        print("Current IP [ERROR]")
        f2 = open(Current_IP,"w")
        GetCurrentIP = os.popen("curl ifconfig.me")
        CIP = GetCurrentIP.read()
        f2.write (CIP)
        f2.close
        print("Current IP [CREATED]")


def Get_Current_IP():
    l1 = open("log.txt","a+")
    print ("Getting Current...")
    GetCurrentIP = os.popen("curl ifconfig.me")
    CIP = GetCurrentIP.read()
    l1.write(sttime+" <INFO> "+" Checking Current IP \n")
    f2 = open(Current_IP,"w")
    f2.write (CIP)
    f2.close

def Email():
    if os.path.isfile("settings.conf"):
        email_address_r = open("settings.conf","r")
        email_username = email_address_r.readlines()[1]
        if email_username == "":
            print("No Email Stored check your settings.conf file")
        else:
            password_r = open("settings.conf","r")
            email_password = password_r.readlines()[2]
            if email_password == "":
                print("No Password has been stored check your settings.conf file")
            else:
                f = open("ips/currentip.txt","r")
                IP_Address = f.read()
                sent_from = email_username
                sent_to = email_username
                subject = "IP Address has changed"
                body = "Your new IP address is : " + str(IP_Address)
                email_text = """\
                        From: %s
                        To: %s
                        Subject: %s
                        %s
                        """ % (sent_from, ", ".join(sent_to), subject, body)
                try:
                            server = smtplib.SMTP_SSL("smtp.gmail.com",465)
                            server.ehlo()
                            server.login(email_username, email_password)
                            server.sendmail(sent_from,sent_to,email_text)
                            server.close()
                            print ("Email Has Been Sent")
                except:
                            print ("Something went wrong...")
    else:
        print ("Error no config file found")
        create_config = input ("Do you wish to Create a config file (Y or N): ")
        if create_config == "Y":
            f = open("settings.conf","a+")
            email_username = input("enter username: ")
            email_password = input("Enter Password: ")
            f.write(str(email_username)+"\n")
            f.write(str(email_password))
            f.close()
            print ("config file created ")
        else:
            print ("Exiting program")
            
def Matrix():
    print("Using Matrix")


def SMS():
    print("Using SMS")


    
def Main():
    Current_IP_Check()
    Last_IP_Check()
    f1 = open(Current_IP,"r")
    CIP = f1.read()
    f2 = open(Last_IP,"r")
    LIP = f2.read()
    Same_IP = False
    print ("Current ip is: "+ CIP)
    print ("Last IP was: "+ LIP)
    if CIP == LIP:
        Same_IP == True
        l1 = open("log.txt","a+")
        l1.write(sttime+" <INFO> -"+" IP is unchanged"+"\n")
    else:
        Same_IP == False
        print ("IP has changed!")
        l1 = open("log.txt","a+")
        print ("New IP Detected")
        l1.write(sttime+" <INFO> -"+" New IP Detected "+"\n")
        Get_Current_IP()
        l1.write(sttime+" <INFO> -"+" New IP Updated: "+str(Current_IP)+"\n")
        os.system("cp ips/currentip.txt ips/lastip.txt")
        print("IP Address Updated")
        l1.close()
        print (contact_method)
        if contact_method == "Email":
            Email()
        elif contact_method == "Matrix":
            Matrix()
        elif contact_method == "SMS":
            SMS()
        else:
            print ("No Contact Method Set ")


Main()