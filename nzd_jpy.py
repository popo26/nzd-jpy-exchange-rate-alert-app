#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import datetime as dt
import time
import smtplib
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.currencyapi.com/v3/latest"
API_KEY = getenv("API_KEY")

MY_EMAIL = getenv("MY_EMAIL")
MY_PASSWORD = getenv("MY_PASSWORD")


params = {
    'apikey': API_KEY,
    'base_currency': 'NZD',
    'currencies': "JPY",
}


while True:
    time.sleep(1)
    if dt.datetime.now().time().strftime("%H:%M:%S")  == '09:00:00':

        response = requests.get(BASE_URL, params=params)
        data = response.json()
       
        jpy = data['data']['JPY']['value']
        message = f' JPY is {jpy} yen now.'

        if jpy < 78:

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL, 
                    to_addrs=MY_EMAIL, 
                    msg=f"Subject:NZD/JPY is now below 76yen\n\n{message}")

