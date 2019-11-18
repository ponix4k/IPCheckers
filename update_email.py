#! /usr/bin/python3
import smtplib
import os
import sys

if os.path.isfile("settings.conf"):
    s0 = open("settings.conf","r")
    email_username = s0.readlines()[0]
    if email_username == "":
        print("No username stored check settings.conf")
    else:
        s1 = open("settings.conf","r")
        email_password = s1.readlines()[1]
        if email_password == "":
            print("No Password Stored check settings.conf")
        else:
            f = open("currentip.txt","r")
            Ip_Address = f.read()
            sent_from = email_username
            sent_to = email_username
            subject = 'IP Address has changed'
            body = 'New IP address is: ' + str(Ip_Address)
            email_text =  """\
            from: %s
            To: %s
            Subject: %s
            %s
            """ % (sent_from, ", ".join(sent_to), subject, body)
            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com',465)
                server.ehlo()
                server.login(email_username, email_password)
                server.sendmail(sent_from,sent_to,email_text)
                server.close()
                print ('Email Has Been Sent')
            except:
                print ('Something went wrong...')
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

