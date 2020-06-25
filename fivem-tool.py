import os
import time
import requests
import subprocess
import urllib
import webbrowser
import colorama
from colorama import Fore
import shutil
import ctypes, sys
import random
import string

colorama.init()


homepath = os.path.expanduser(os.getenv('USERPROFILE'))

ctypes.windll.kernel32.SetConsoleTitleW(f"fivem-tool | made by: hunchos")


clear = lambda : os.system("cls")


def wylaczproces(nazwa):
    os.system("taskkill /f /im " + nazwa)


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def login():

    haslo = randomString(10)

    print(f'Your password: {haslo}')
    password = str(input("> "))


    if password == haslo:
        print(f"{Fore.GREEN}Logged in!")
    else:
        print(f"{Fore.RED}Wrong password!{Fore.RESET}")
        login()

login()
def deletingfivem():

    wylaczproces('FiveM.exe')
    wylaczproces('Steam.exe')

    print('Deleting Temp Folder')
    shutil.rmtree(homepath + '/AppData/Local/Temp', ignore_errors=True)
    time.sleep(3)

    print('Deleting DigitalEntitlements folder')
    shutil.rmtree(homepath + '/AppData/Local/Temp/DigitalEntitlements', ignore_errors=True)

    print('Deleting CitizenFX files')
    shutil.rmtree(homepath + '/AppData/Roaming/CitizenFX', ignore_errors=True)
    shutil.rmtree(homepath + '/Saved Games/CitizenFX', ignore_errors=True)

print(f'''{Fore.CYAN}
   __ _                         _              _ 
  / _(_)                       | |            | |
 | |_ ___   _____ _ __ ___     | |_ ___   ___ | |
 |  _| \ \ / / _ \ '_ ` _ \    | __/ _ \ / _ \| |
 | | | |\ V /  __/ | | | | |   | || (_) | (_) | |
 |_| |_| \_/ \___|_| |_| |_|    \__\___/ \___/|_|
 
           {Fore.CYAN}### {Fore.RED}made by: hunchos{Fore.CYAN} ###
''')


print(f'Select your option')

choice = input('''
[ 1 ] FiveM CitizenFX deleter ( fivem local storage deleter ) 
[ 2 ] DISCORD_RPC disabler
''')

if choice == ('1'):
    clear()

    choice = input('Are you sure [y/n]: ')
    if choice == ('y'):

        deletingfivem()

    if choice == ('n'):
        exit()


if choice == ('2'):

    print('disabling discord_rpc')
    os.rename(homepath + '/AppData/Roaming/Discord/0.0.306/modules/discord_rpc', homepath + '/AppData/Roaming/Discord/0.0.306/modules/discord_rpc.disabled')
    print('discord_rpc disabled')

input('Done! Press enter to exit')