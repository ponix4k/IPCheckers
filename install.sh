#!/bin/sh
#crontab -l > crontab.txt
#echo "### Crontask for IP Checker  ###" >> crontab.txt
#echo "* * * * *  cd ~/IPCheckers && /usr/bin/python3.7 test.py" >> crontab.txt
crontab `pwd`/crontab.txt
rm `pwd`/crontab.txt
sudo apt-get install python3-pip -y
pip3 install -r requirements.txt