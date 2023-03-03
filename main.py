from requests import get
from subprocess import Popen
from time import sleep
from os import remove, path

i = 0
version = 2
# updated to version 2


def check_version():
    return int(get("https://raw.githubusercontent.com/TheFlighteur/python-updater/main/version").text)


def check_for_update():
    if check_version() > version:
        print("updating script")
        bootstrap_updater()
        Popen(f"python updater.py")
        quit()


def bootstrap_updater():
    f = open("updater.py", "w")
    f.write("""from requests import get
from time import sleep
from subprocess import Popen
sleep(1)
f = open("main.py", "w")
f.write(get("https://raw.githubusercontent.com/TheFlighteur/python-updater/main/main.py").text)
f.close()
Popen("python main.py")
""")
    f.close()


if path.exists("updater.py"):
    print("deleting updater")
    remove("updater.py")
while i < 100:
    print(i)
    i += 1
    sleep(1)
    check_for_update()
