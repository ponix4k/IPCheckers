
import re ,os ,sys
import requests
from datetime import datetime
from pathlib import Path as plib 

log_path = 'log.txt'
last_ip = 'last_ip.txt'
current_ip = 'functions/current_ip.txt'

def check_exists(file_path):
  p = plib(file_path)
  ret_val = False
  if p.is_dir():
    ret_val = True

def get_currentip():
    url =  'https://ifconfig.me/ip'
    with open(current_ip, 'w+') as f:
        r = requests.get(url, data=f)
        f.write(str(r.text))

def read_last_ip():
      with open('./functions/last_ip.txt', 'r') as ip_file:
        last_ip = ip_file.read()
        print(f'Last IP was: {last_ip}')
        return last_ip

def read_current_ip():
      with open('./functions/current_ip.txt', 'r') as cip:
        current_ip = cip.read()
        print(f'Current IP is: {current_ip}')
        return current_ip

def log_change(cip, lip):
    if cip == lip:
        print("all ok")
    else:
        print("IP Address has changed")
  
#get_currentip()
#log_change ( read_last_ip(), read_current_ip() )
    