import os, subprocess

path = '/Users/'+os.getlogin()+'/loaner_reminder/toast.py'

command = str(subprocess.check_output("which python3", shell=True))[2:-3]

os.system("crontab -l | grep -v \'"+ command + " " + path + "\'  | crontab -")
