#!/bin/sh
crontab -l > crontab.txt
echo "### Crontask for IP Checker  ###" >> crontab.txt
echo "* * * * *  cd ~/IPCheckers && /usr/bin/python3.7 main.py" >> crontab.txt
crontab `pwd`/crontab.txt
rm `pwd`/crontab.txt
mkdir `pwd`/ips -p
echo "0.0.0.0" > `pwd`/ips/last_ip.txt
echo "0.0.0.0" > `pwd`/ips/current_ip.txt
sudo apt-get install python3-pip -y
pip3 install -r requirements.txt