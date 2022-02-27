from ast import If
import requests
from bs4 import BeautifulSoup
import difflib
import schedule
import time
from datetime import datetime
from urllib.error import URLError
from urllib.error import HTTPError
import os

# Global variable declaration

Intensity = 1

# TASK 1
Counter_1 = 0
ErrorCounter_1 = 0

# End of global variable declaration



urls = [
    'https://lenta.ru/',
    'https://ria.ru/',
    'https://ria.ru/lenta/',
    'https://www.rbc.ru/',
    'https://www.rt.com/',
    'http://kremlin.ru/',
    'http://en.kremlin.ru/',
    'https://smotrim.ru/',
    'https://tass.ru/',
    'https://tvzvezda.ru/',
    'https://vsoloviev.ru/',
    'https://www.1tv.ru/',
    'https://www.vesti.ru/',
    'https://online.sberbank.ru/',
    'https://sberbank.ru/',
    'https://zakupki.gov.ru/',
    'https://www.gosuslugi.ru/',
    'https://er.ru/',
    'https://www.rzd.ru/',
    'https://rzdlog.ru/',
    'https://vgtrk.ru/',
    'https://www.interfax.ru/',
    'https://www.mos.ru/uslugi/',
    'http://government.ru/',
    'https://mil.ru/',
    'https://www.nalog.gov.ru/',
    'https://customs.gov.ru/',
    'https://pfr.gov.ru/',
    'https://rkn.gov.ru/',
    'https://www.gazprombank.ru/',
    'https://www.vtb.ru/',
    'https://www.gazprom.ru/',
    'https://lukoil.ru',
    'https://magnit.ru/',
    'https://www.nornickel.com/',
    'https://www.surgutneftegas.ru/',
    'https://www.tatneft.ru/',
    'https://www.evraz.com/ru/',
    'https://nlmk.com/',
    'https://www.sibur.ru/',
    'https://www.severstal.com/',
    'https://www.metalloinvest.com/',
    'https://nangs.org/',
    'https://rmk-group.ru/ru/',
    'https://www.tmk-group.ru/',
    'https://ya.ru/',
    'https://www.polymetalinternational.com/ru/',
    'https://www.uralkali.com/ru/',
    'https://www.eurosib.ru/',
    'https://omk.ru/',
    'https://mail.rkn.gov.ru/',
    'https://cloud.rkn.gov.ru/',
    'https://mvd.gov.ru/',
    'https://pwd.wto.economy.gov.ru/',
    'https://stroi.gov.ru/',
    'https://proverki.gov.ru/',
    'https://www.gazeta.ru/',
    'https://www.crimea.kp.ru/',
    'https://www.kommersant.ru/',
    'https://riafan.ru/',
    'https://www.mk.ru/',
    'https://api.sberbank.ru/prod/tokens/v2/oauth',
    'https://api.sberbank.ru/prod/tokens/v2/oidc'
]
print("************************************")
print("* !!! STOP WAR !!! STOP RUSSIA !!! *")
print("************************************")
print("")
print("**********************************************************************************************************************")
print("* See! The beacons of Gondor are alight, calling for aid. War is kindled.                                            *")
print("* See, there is the fire on Amon Dîn, and flame on Eilenach;                                                         *")
print("* and there they go speeding west: Nardol, Erelas, Min-Rimmon, Calenhad, and the Halifirien on the borders of Rohan. *")
print("* - Gandalf | The Return of the King. -                                                                              * ")
print("**********************************************************************************************************************")
print("")
print("********************************")
print("* !!! LIGHT UP YOUR BEACON !!! *")
print("********************************")
print("")
print("Together, we can help to stop Vladimir Putin's regime, which kills innocent people.")
print("All Russian official news websites are fake and best solution is to shut them down!")
print("Keep this script running. This script will check listed websites until they begin to spread the truth:")
print("")
print("TARGET LIST:")
print(*urls, sep = ", ")
print("")
print("!!! TOGETHER WE CAN SEND A MESSAGE TO PUTIN - GO TO HELL !!!")
print("")
print("Please enter the amount of your anger. 1 - light | 2 - moderate | 3 - severe")
Input = int(input ("Enter number (1, 2 or 3): "))

if Input == 1:
    Intensity = 1

if Input == 2:
    Intensity = 0.1
    
if Input == 3:
    Intensity = 0.01

def job1():
    
    global Counter_1
    global ErrorCounter_1
    global Intensity
    
    # be like browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    #with requests.Session() as s:
    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=Intensity)           
        except requests.ConnectionError:
            response = ""
            ErrorCounter_1 = ErrorCounter_1 + 1
            print("IS DOWN URL: "+url + "" +" | URL Hit Counter: " + str(Counter_1) +" | URL Shutdown/Error Counter: " + str(ErrorCounter_1) + " | TIME: " +str(datetime.now()))
        except HTTPError as http_error: 
            print("IS DOWN URL: "+url + "" +" | URL Hit Counter: " + str(Counter_1) +" | URL Shutdown/Error Counter: " + str(ErrorCounter_1) + " | TIME: " +str(datetime.now()))
            ErrorCounter_1 = ErrorCounter_1 + 1
        except URLError as url_error: 
            print("IS DOWN URL: "+url + "" +" | URL Hit Counter: " + str(Counter_1) +" | URL Shutdown/Error Counter: " + str(ErrorCounter_1) + " | TIME: " +str(datetime.now()))
            ErrorCounter_1 = ErrorCounter_1 + 1
        except (requests.exceptions.RequestException, ValueError) as e:
            print("IS DOWN URL: "+url + "" +" | URL Hit Counter: " + str(Counter_1) +" | URL Shutdown/Error Counter: " + str(ErrorCounter_1) + " | TIME: " +str(datetime.now()))
            ErrorCounter_1 = ErrorCounter_1 + 1
        else: 
            Counter_1 = Counter_1 + 1
            print("HIT URL: "+url + "" +" | URL Hit Counter: " + str(Counter_1) +" | URL Shutdown/Error Counter: " + str(ErrorCounter_1) + " | TIME: " +str(datetime.now()))

 
schedule.every(Intensity).seconds.do(job1) # JOB 1

schedule.run_all()
while True:
    schedule.run_pending()
    time.sleep(Intensity)