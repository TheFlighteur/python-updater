import requests
import pathlib
from subprocess import Popen
from time import sleep
i = 0
version = 1
currpath = pathlib.Path(__file__).parent.resolve()

def check_version():
    online_version = requests.get("https://raw.githubusercontent.com/TheFlighteur/python-updater/main/version")
    return int(online_version.text)


def check_for_update():
    if check_version() > version:
        print("updating script")
        bootstrap_updater()
        Popen("python {}/{}".format(currpath, "updater.py"))
        quit()


def bootstrap_updater():
    f = open("./updater.py", "w")
    f.write("""from requests import get
from time import sleep
sleep(1)
f = open("./main.py", "w")
f.write(get("https://raw.githubusercontent.com/TheFlighteur/python-updater/main/main.py").text)
f.close()
""")
    f.close()


while i < 100:
    print(i)
    i += 1
    sleep(1)
    check_for_update()
