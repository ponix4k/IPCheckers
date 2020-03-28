#!/usr/bin/env python3
import smtplib,ssl
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
        #print(settings)
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
            server = smtplib(settings.email_server, settings.email_port)
            print(server)
            server.ehlo()
            print("ehlo")
            server.login(settings.email_user, settings.email_password)
            print(server.login)
            server.sendmail(settings.email_user, settings.to, settings.message)
            print (server.sendmail)
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
            "id": "x",
            "is_enabled": True,
            "username": "email@email.com",
            "password": "hunter2",
            "subject": "IP HAS CHANGED",
            "message":"Your new IP address is: ",
            "email_server": "smtp.gmail.com",
            "email_port": "465" 
    }
   
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
            "id": "x",
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
    current_IP = os.popen("curl ifconfig.me").read()
    #print("Current IP is: ",current_IP)
    return current_IP
    
def read_IP_log():
    with open(IP_log) as IPlog:
        last_IP = IPlog.read()
        #print ("Logged IP is: " +logged_IP)
        return last_IP
        IPLog.close()

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
        
def main():
    has_changed = False
    settings = read_settings()
    current_IP = get_IP_address()
    last_IP = read_IP_log()
    #print("Current ip is: ",current_IP)
    #print("Last IP is: ",last_IP)
    #print("has_changed: ",has_changed)
    if current_IP != last_IP:
        has_changed = True
    else:
        has_changed = False

    print (has_changed)
    printnotif = notification("your IP is: " + str(current_IP))
    printnotif.send_message()
    if (has_changed):
        email = email_notification(current_IP,settings["email"])
        #print (email)
        send(email)
    
if __name__ == "__main__":
    main()
