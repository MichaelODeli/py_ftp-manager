# import useful modules
from ftplib import FTP
import configparser
from win10toast import ToastNotifier
from pymsgbox import * # не обязательно
import time

# config reader
# на вход идет файл с настройками, в котором внутренние папки прописаны через запятую
# мы разбиваем эту строку на список, по которому будем следовать и входить в нужную внутреннюю директорию
set_name='settings.ini' # settings name file
config=configparser.ConfigParser(comment_prefixes=';', inline_comment_prefixes=';') # config file param
config.read("settings.ini") # open config file
hosturl=config.get('ftp_param', 'host')
folder_list=config.get('ftp_param', 'folder')
ftplogin=config.get('ftp_param', 'login')
ftppassword=config.get('ftp_param', 'password')
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
# ftp.retrlines('LIST') - полный список файлов с их правами и временем-датой создания
data_launch = ftp.nlst()
print("Press CTRL+C for stop monitoring")

# notification set-up
def show_alert():
    alert(text='Feature is not ready for use', title='Warning', button='OK') #не обязательно
toaster = ToastNotifier()

# monitoring
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
            time.sleep(5)
    except KeyboardInterrupt:
        break
