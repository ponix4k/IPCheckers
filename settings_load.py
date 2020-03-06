#!/usr/bin/env python3
import os
import sys
import xml.etree.ElementTree as ET

tree = ET.parse('test_settings.xml')
root = tree.getroot()
tag = root.tag
attribute = root.attrib
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
            print("No Active contact methods")







#def load_xml_settings():
#    if os.path.isfile('settings.xml'):
#        print('Settings found!')
#        config = MD.parse('settings.xml')
#        settings = config.getElementsByTagName('settings')
 #       for setting in settings:
 #           username = (settings['email_user'])

#load_xml_settings()


# def load_settings(path):
#    settings = {}
#    if os.path.isfile(path):
#        print('file found')
#        with open(path, 'r') as settings_file:
#            settings['contact_method'] = settings_file.readlines()[0].lower()
#            if (settings['contact_method'] == 'email'):
#                settings['email_user'] = settings_file.readlines()[1]
#                if (check_setting_is_empty(settings['email_user'])):
#                    print('no email found in cmeig file')
#                settings['email_password'] = settings_file.readlines()[2]
#                if (check_setting_is_empty(settings['email_password'])):
#                    print('no password found in config file')
#            else:
#                print('no contact method selected')
#            print(settings)
#            settings_file.close()
#    else:
#        create_settings_file(path, settings)
#    return settings
