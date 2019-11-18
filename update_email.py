#! /usr/bin/python3

import smtplib
s0 = open("settings.conf","r")
gmail_username = s0.readlines()[0]
s1 = open("settings.conf","r")
gmail_password = s1.readlines()[1]

f = open("currentip.txt","r")
Ip_Address = f.read()
sent_from = gmail_username
sent_to = gmail_username
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
    server.login(gmail_username, gmail_password)
    server.sendmail(sent_from,sent_to,email_text)
    server.close()
    print ('Email Has Been Sent')
except:
    print ('Something went wrong...')
