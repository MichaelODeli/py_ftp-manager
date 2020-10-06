# import  modules
from ftplib import FTP
import configparser
from win10toast import ToastNotifier
from pymsgbox import *
import time

# config reader
# the input is a file with settings, in which the internal folders are spelled out with commas
# we split this line into a list, which we will follow and enter into the desired internal directory
set_name='settings.ini' # settings name file
config=configparser.ConfigParser(comment_prefixes=';', inline_comment_prefixes=';') # config file param
config.read("settings.ini") # open config file
hosturl=config.get('ftp_param', 'host')
folder_list=config.get('ftp_param', 'folder')
ftplogin=config.get('ftp_param', 'login')
ftppassword=config.get('ftp_param', 'password')
tmemon=int(config.get('main', 'tmemon'))
folder_list=folder_list.split(",")
folders_number=len(folder_list)

#ftp set-up
ftp=FTP(hosturl)
try:
    ftp.login()
except:
    ftp.login(ftplogin, ftppassword)
for folder_name in folder_list:
    ftp.cwd(folder_name)
data_launch = ftp.nlst()

# notification set-up
def show_alert():
    alert(text='Feature is not ready for use', title='Warning', button='OK') #не обязательно
toaster = ToastNotifier()

# output text
print("Welcome to FTP Manager!")
print("Before you start using the program, have you checked the settings.ini file? If yes, then enter 'y', if not, then 'n'")
checker=str(input())
if checker=='n' :
    raise SystemExit('Check your settings.ini file')
if checker=='y':
        # file monitoring
    print("Press CTRL+C for stop monitoring")
    n=5
    while n>0:
        try:
            data = ftp.nlst()
            if data != data_launch:
                toaster.show_toast("FTP Manager", #title
                        "Some files has been updated. Click to view.", #description
                        duration=1,
                        callback_on_click=show_alert)
                data_launch=data
                time.sleep(tmemon)
        except KeyboardInterrupt:
            break
else:
    raise SystemExit('Invalid input.')