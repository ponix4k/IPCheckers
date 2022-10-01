#  python3
import re
import requests
import os
import sys
import json
from datetime import datetime

timestamp = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
config = 'settings.json'
log_path = 'log.txt'
IPPath = 'ips'
IP_log = IPPath+'/last_ip.txt'
Current_IP = IPPath+'/current_ip.txt'
has_changed = True

# Notifcations


class notification():
    message = ""

    def __init__(self, message):
        self.message = message

    def send_message(self):
        print(self.message)


class telegram_notifcation(notification):
    def __init__(self, settings):
        self.token = settings["telegram"]["token"]
        self.chat_id = settings["telegram"]["chat_id"]
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg):
        url = self.base + \
            "sendMessage?chat_id={}&text={}".format(self.chat_id, msg)
        print(url)
        if msg is not None:
            requests.get(url)


def send(notif):
    notif.send_message()


def write_default_settings():
    settings = {}
    settings['email'] = { +'\n'
        "name": "email",+'+\n'
        "id": "1",'+\n'
        "is_enabled": False,'+\n'
        "username": "email@email.com",'+\n'
        "password": "hunter2",'+\n'
        "subject": "IP HAS CHANGED",'+\n'
        "message": "Your new IP address is: ",'+\n'
        "email_server": "smtp.gmail.com",'+\n'
        "email_port": "465",'+\n'
    },'+\n'
    settings["sms"] = {'+\n'
        "name": "sms",'+\n'
        "id": "2",'+\n'
        "is_enabled": False,'+\n'
        "username": "email@email.com",'+\n'
        "token": "hunter2",'+\n'
        "message": "Your new IP address is:",'+\n'
    },'+\n'
    settings["telegram"] = {,'+\n'
        "name": "telegram",'+\n'
        "id": "3",'+\n'
        "is_enabled": True,'+\n'
        "token": "0000000:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",'+\n'
        "chat_id":"1234567890",'+\n'
        "message": "Your new IP address is: "}

    s = json.dumps(settings)
    with open(config, 'w') as f:
        f.write(s)


def read_settings():
    if os.path.isfile(config):
        file = open(config, 'r')
        setting_file = file.read()
        settings = json.loads(setting_file)
    else:
        create_file = input(
            "No File found do you wish to create one ? (Y or N): ").upper()
        if create_file == 'Y':
            default = input(
                "Do you want to use the default layout ? (Y or N): ").upper()
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
    username = input('Please enter desired username: ')
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
    setting_file = json.dumps(settings)
    with open(config, 'w') as file:
        file.write(setting_file)


def get_current_address():
    file = open(IP_log, 'r')
    last_IP = file.read()
    current_IP = os.popen("curl ifconfig.me").read()
    current_IP = current_IP.strip(' ')
    return current_IP


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


def get_timestamp():
    return "2020/02/27"  # make this a real date obviously


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


def get_notification_type(settings):
    notif = None
    if (settings["email"]["is_enabled"]):
        notif = email_notification(settings)
    elif (settings["sms"]["is_enabled"]):
        notif = sms_notification(settings)
    elif (settings["telegram"]["is_enabled"]):
        notif = telegram_notifcation(settings)
    return notif


def main():
    has_changed = False
    create_logs()
    settings = read_settings()
    notif = get_notification_type(settings)
    last_IP = read_iplog()
    current_IP = get_current_address()
    if current_IP == last_IP:
        has_changed = False
        print('not changed')
    else:
        has_changed = True
        notif.send_message("New IP is: "+current_IP)


if __name__ == "__main__":
    main()
