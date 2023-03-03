from requests import get
from subprocess import Popen
from time import sleep
from datetime import datetime

i = 0
version = 3
# updated to version 3


def check_version():
    return int(get("https://raw.githubusercontent.com/TheFlighteur/python-updater/main/version").text)


def check_for_update():
    if check_version() > version:
        print("updating script")
        f = open(__file__, "w")
        f.write(get("https://raw.githubusercontent.com/TheFlighteur/python-updater/main/main.py").text)
        f.close()
        Popen(f"python main.py")
        quit()

        
u = open("updated.txt", "a")
u.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
u.close()
while i < 100:
    i += 1
    sleep(1)
    check_for_update()
