import requests
import pathlib
from subprocess import Popen

version = 1
currpath = pathlib.Path(__file__).parent.resolve()

def check_version():
    online_version = requests.get("https://raw.githubusercontent.com/TheFlighteur/python-updater/main/version")
    return int(online_version.text)


def check_for_update():
    if check_version() > version:
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
