#!/usr/bin/env python3
import smtplib 
import os,sys
class notification():
    message = ""

    def __init__(self):
       self.message = "message"

    def send_message(self):
        print(self.message)

class email_notification(notification):
    import smtplib
    
    def __init__(self, message, settings):
        self.email_user = settings["email_user"]
        self.email_password = settings["email_password"]
        self.message = message
        
        self.to = settings["to"]
        self.subject = settings["subject"]
        self.email_server = settings["email_server"]
        self.email_port = settings["email_port"]

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



def check_setting_is_empty(setting):
    if len(setting > 0):
        return False
    else:
        return True

def create_settings_file(path, settings):
    settings["contact_method"] = input("enter contact method:").lower()
    settings["email_user"] = input("enter email user:").lower()
    settings["email_password"] = input("enter password:")
    settings["to"] = input("enter recipient:")
    settings["email_server"] = "smtp.gmail.com"
    settings["email_port"] = 465
    settings["subject"] = "IP Address Update"

    with open(path, 'a+') as settings_file:
        for key,value in settings.items():
            settings_file.write("{}\n".format(value))

    settings_file.close()
    return settings


def load_settings(path):
    settings = {}
    if os.path.isfile(path):
        print("file found")
        with open(path, 'r') as settings_file:
            
            settings["contact_method"] = settings_file.readlines()[0].lower()
            if (settings["contact_method"] == "email"):
                settings["email_user"] = settings_file.readlines()[1]
                if (check_setting_is_empty(settings["email_user"])):
                    print("no email found in config file")
                settings["email_password"] = settings_file.readlines()[2]
                if (check_setting_is_empty(settings["email_password"])):
                    print("no password found in config file")
            else:
                print("no contact method selected")
            
            print(settings)
            settings_file.close()
    else:
        create_settings_file(path, settings)
    return settings

def get_IP_address():
    return "127.0.0.1"
    
def main():
    settings = load_settings("settings.conf")
    printnotif= notification()
    email= email_notification("your IP is {}".format(get_IP_address()), settings)
    send(printnotif)
    send(email)


if __name__ == "__main__":
    main()