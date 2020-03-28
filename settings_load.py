#!/usr/bin/env python3
import os
import sys
import xml.etree.ElementTree as ET

def load_settings():
    if os.path.isfile('test_settings.xml'):
        print ("Settings File Found")
        tree = ET.parse('test_settings.xml')
        root = tree.getroot()
        for settings in root.findall('contact_method'):
                att = settings.attrib
                #print(att)
                name=att.get('name')
                enabled =att.get('is_enabled')
                #print(enabled)
                if enabled == 'True':
                    print(name,': ',enabled)
                    username=settings.find('username').text
                    password=settings.find('password').text
                    email_server=settings.find('email_server').text
                    email_port=settings.find('email_port').text
                    subject=settings.find('subject').text
                    print ('#################\n',username,':',password,'\n',email_server,':',email_port,'\n',subject,'\n#################')
    else:
        print ("No settings file could be located")
load_settings()

