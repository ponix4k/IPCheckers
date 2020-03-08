#!/usr/bin/env python3
import smtplib
import os,sys
import json
from datetime import datetime

timestamp = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
config = 'settings.json'
log_path = 'log.txt'
IP_log = 'ips/last_ip.txt'
global has_changed 
class notification():
    message = ""

    def __init__(self, message):
       self.message = message

    def send_message(self):
        print(self.message)
        
class email_notification(notification):
    
    def __init__ (self, ip, settings):
        print(settings)
        self.email_user = settings["username"]
        self.email_password = settings["password"]
        self.message = ["message"]
        self.to = settings["username"]
        self.subject = settings["subject"]
        self.email_server = settings["email_server"]
        self.email_port = settings["email_port"]
        self.ip = ip
        

    def send_message(self):
        try:
            server = smtplib.SMTP_SSL(self.email_server, self.email_port)
            server.ehlo()
            server.login(self.email_user, self.email_password)
            server.sendmail(self.email_user, self.to, self.message)
            server.close()
            print("Email Has Been Sent")
        except:
           print("shit went wrong")

def send(notif):
    notif.send_message()
    
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
            "email_port": "465" }
 

    s=json.dumps(settings)
    with open (config,'w') as f:
        f.write(s)

def read_settings():
    if os.path.isfile(config):
        file=open(config,'r')
        setting_file=file.read()
        settings = json.loads(setting_file)
    else:
        create_file = input("No File found do you wish to create one ? (Y or N): ").upper()
        if create_file == 'Y':
            default = input("Do you want to use the default layout ? (Y or N): ").upper()
            if default == 'Y':
                write_default_settings()
            else:
                 write_settings()
        else: 
            print("Exiting Program")
            sys.exit()
    return settings
            
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
    setting_file=json.dumps(settings)
    with open (config,'w') as file:
        file.write(setting_file)
  
def get_IP_address():
    return os.popen("curl ifconfig.me").read()

def read_IP_log():
    with open(IP_log) as IPlog:
        logged_IP = IPlog.read()
        print ("Logged IP is: " +logged_IP)
    IPlog.close()
    return logged_IP

def get_timestamp():
    return "2020/02/27" # make this a real date obviously

def log_IP_change(old_IP, new_IP):
    with open(log_path, "a+") as log:
        log.write("[{}] <INFO> IP Address Changed! Updating\n".format(get_timestamp()))
        log.write("[{}] <INFO> New Address: {}\n\t\t Old Address:{}".format(get_timestamp(), new_IP, old_IP))
        with open(IP_log, "w") as iplog:
            iplog.write(new_IP)
            iplog.close()
        log.close()

def get_current_IP_address():
    current_IP = get_IP_address()
    if os.path.isfile(IP_log):
        logged_IP = read_IP_log()
        if (logged_IP == current_IP): #if they don't match IP has changed - do stuff
            has_changed = False
            return current_IP
        else:
           log_IP_change(logged_IP, current_IP)
           print(logged_ip,current_ip)
           has_changed = True
    else:
        log_IP_change("0.0.0.0",current_IP)
        has_changed = True
        return current_IP
        
def main():
    has_changed = False
    settings = read_settings()
    currentip = get_current_IP_address()
    print(has_changed)
    #printnotif = notification("your IP is: " + str(currentip))
    #printnotif.send_message()
    if (has_changed):
        email = email_notification(currentip,settings["email"])
        send(email)
    
if __name__ == "__main__":
    main()
