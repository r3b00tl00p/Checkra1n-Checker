#Checkra1n Checker for MacOS by r3b00tl00p
#Original code by wink05

#place for imports
import time
from os import system
import os
import requests

def clear():
        _ = system('clear')

def check():
    r = requests.get("http://checkra.in/index.html", allow_redirects=True)
    open('index.html', 'wb').write(r.content)
    print("[Download done.]")
    t = time.localtime()
    current_time = time.strftime("%d.%m.%Y, %H:%M %z")
    with open('index.html') as f:
        if 'eta son' in f.read():
            print(current_time + ": Checkra1n is not released yet :-(")
        else:
            print(current_time + ": Checkra1n IS RELEASED !!!")
    os.remove('index.html')
    time.sleep(300)
    #Modify the numeric value (300 by default) to change the time between 2 refresh (in seconds)
    clear()

while True:
    clear()
    check()
