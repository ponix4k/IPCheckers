#!/usr/bin/env python3
import os
import sys
import json

config = 'test_settings.json'

def read_settings():
    if os.path.isfile(config):
        f=open(config,'r')
        s=f.read()
        settings = json.loads(s)
        is_enabled = settings['email']['is_enabled']
        username  = settings['email']['username']
        passwd  = settings['email']['password']
        server = settings['email']['email_server']
        port = settings['email']['email_port']
        subject = settings['email']['subject']
        message = settings['email']['message']
        print(is_enabled)
        print(username,':',passwd)
        print(server,':',port)
        print(subject,'\n',message)
    else:
        create_file = input("No File found do you wish to create one ? (Y or N): ").upper()
        if create_file == 'Y':
            default = input("Do you want to use the default layout ? (Y or N): ").upper()
            if default == 'Y':
                write_settings()
            else:
                 write_default_settings()
        else: 
            print("Exiting Program")
            
read_settings()

def write_settings():
    settings = {}
    name = input('Please enter the name of the contact method: ')
    enabled = input('Do you want this method to be enabled(true or false): ')
    username = input('Please eenter desired username: ')
    passwd = input('Please enter desired password: ')
    subject = input('Please enter desired subject: ')
    message = input('Please enter the desired message: ')
    server = input('Please enter the address of the server you wish to user: ')
    port = input('Please set the port you wish to use: ')
    
    
    settings['email'] = {
            "name": name,
            "id": "1",
            "is_enabled": enabled,
            "username": username,
            "password": passwd,
            "subject": subject,
            "message": message,
            "email_server": server,
            "email_port": port 
    }
    s=json.dumps(settings)
    with open (config,'w') as f:
        f.write(s)
    #print(s)
#write_settings()


def write_default_settings():
    settings = {}
    settings['email'] = {
            "name": "email",
            "id": "1",
            "is_enabled": True,
            "username": "email@email.com",
            "password": "hunter2",
            "subject": "IP HAS CHANGED",
            "message":"Your new IP address is: ",
            "email_server": "smtp.gmail.com",
            "email_port": "465" 
    }
    settings['matrix'] = {
            "name": "matrix",
            "id": "2",
            "is_enabled": False,
            "username": "email@email.com",
            "password": "hunter2",
            "subject": "IP HAS CHANGED",
            "message":"Your new IP address is: ",
            "email_server": "smtp.gmail.com",
            "email_port": "465" 
    }
    settings['telegram'] = {
            "name": "matrix",
            "id": "3",
            "is_enabled": False,
            "subject": "IP HAS CHANGED",
            "message":"Your new IP address is: ",
            "phone_number":"0123456789"
    }
    settings['sms'] = {
            "name": "sms",
            "id": "4",
            "is_enabled": False,
            "subject": "IP HAS CHANGED",
            "message":"Your new IP address is: ",
            "phone_number":"0123456789"
    }

    s=json.dumps(settings)
    with open (config,'w') as f:
        f.write(s)
#write_default_settings()
