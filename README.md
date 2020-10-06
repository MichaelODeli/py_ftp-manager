# py_ftp-manager
A simple script to track file changes in an FTP directory

## Requirements
```
win10toast (with fix)
configparser
pymsgbox
ftplib
```

## How to fix win10toast
you need to move file `__init__.py` to the directory of your python to support the action on click on the notification
For example, standart directory is: `%localappdata%\Programs\Python\Python38\Lib\site-packages\win10toast`

## How to use
First, you need to open the settings.ini file and specify the settings for your file storage there. All instructions are inside the file
Then, just start the application and follow the instructions
