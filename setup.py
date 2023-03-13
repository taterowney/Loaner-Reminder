import datetime
import sys
import os
import subprocess

if len(sys.argv) < 2:
    interval = '20'
else:
    interval = sys.argv[1]

with open('./data.log', 'w') as f:
    f.write(datetime.datetime.now().isoformat())
    f.write('\n')
    f.write(interval)

path = '/Users/'+os.getlogin()+'/loaner_reminder/toast.py'

command = str(subprocess.check_output("which python3", shell=True))[2:-3]

os.system("crontab -l | grep -v \'"+ command + " " + path + "\'  | crontab -")
os.system("(crontab -l ; echo \"*/20 * * * * " + command + " " + path + "\") | crontab -")
os.system("(crontab -l ; echo \"@reboot " + command + " " + path + "\") | crontab -")
