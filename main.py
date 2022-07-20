#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Rvi

##IMP
#This Script Only Will Work with Iran(+98) Phone Numbers Only

## Apis.JSON FORMAT:
# { URL: [ METHOD , PAYLOAD , RETRY , exRESPONSE , HEADER] }
### HEDAER can be null ###
### $PHONE can Be in headers too ###
### $PHONE allways starts with 9 ###

from src.spammer import Spammer
from colorama import Fore, Style
import json
import sys
import time

RETRY = True

def logo():
    print(Fore.YELLOW, end="")
    print("\n ___  __  __  ___  ____   __    __  __ \n/ __)(  \/  )/ __)(  _ \ /__\  (  \/  )\n\__ \ )    ( \__ \ )___//(__)\  )    ( \n(___/(_/\/\_)(___/(__) (__)(__)(_/\/\_)", end="")
    print(Style.RESET_ALL, end="")
    print("\tby RVI", end="")


def status(v):
    if v == False:
        return "Off"
    else: return "On"


def ifTry():
    ans = str(input("Do you want to continue?(N, Y) "))
    if ans in ("N", "n", "NO"):
        print("By :)")
        sys.exit()
    elif ans == "":
        print("No command received")
        sys.exit()        

def get_number():
    phone_number = str(input("Enter your target PhoneNumber: "))
    if len(phone_number) <= 1:
        print("No number entered. Please try again")
        ifTry()
        return get_number()
    elif len(phone_number) <= 9:
        print("The entered number is not correct")
        ifTry()
        return get_number()
    return phone_number


def get_other():

    try:
        count = int(input("How many time do you want to ReSpam (default is 1): "))
    except:
        count = 1
    delay = 1
    if count > 1:
        try:
            delay = int(input("How Much Delay(sleep) between Spams (default is 180Sec)? ", ))
        except:
            delay = 180


    doLog = str(input("Do You Need Logs For All SMSes?:(Y, N) "))
    if doLog in ("", "Y", "y", "yes"): doLog = True
    else: doLog = False

    return count , delay, doLog



def main():
    
    logo()
    urls = json.load(open("src/apis.json"))
    print("\n\n")
    print(f"{Fore.BLUE}{len(urls)}{Style.RESET_ALL} Urls Loaded from apis.json")
    print(f"Request retry is {Fore.BLUE}{status(RETRY)}{Style.RESET_ALL}")
    print("\n")
    num = get_number()
    reSpamCount, reSpamDelay, smsLogger = get_other()
    if reSpamCount > 1:
        counter = 0
        for i in range(reSpamCount):
            Spammer(num, logger=smsLogger)
            counter+=1
            if counter >= reSpamCount:
                break
            time.sleep(reSpamDelay)
    else:
        Spammer(num, logger=smsLogger)






if __name__=="__main__":
    main()