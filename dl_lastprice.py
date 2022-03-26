
from ib_insync import *
import math
#util.startLoop()

import requests
import json

import pandas as pd
import yfinance as yf
import datetime as dt
from datetime import timedelta
import os
import pickle
import winsound
import time
import sys

symbols =['SHOP.TO', 'HNU.TO', 'HND.TO']

now = dt.datetime.now()
print()
price_dict = {}

from collections import namedtuple 



#out_file = f'C:/data/last/{now.strftime("%Y%m%d")}.json'
out_file = f'C:/data/last/last.json'
if (os.path.exists(out_file)):
    with open(out_file) as json_fp:
        price_dict = json.load(json_fp)
        print(price_dict)

# hack, should compre keys to symbol list
if len(price_dict) != len(symbols):
    for symbol in symbols:
        end = dt.datetime.now() - timedelta(hours=12)
        start = dt.datetime.now() - timedelta(days=5)
        df = yf.download(symbol, start.strftime('%Y-%m-%d'), end=end.strftime('%Y-%m-%d'), progress=False)
        if symbol.endswith('.TO'):
            symbol = symbol.replace('.TO', '.TSE')
        price_dict[symbol] = df["Close"].iloc[-1]

    with open(out_file, 'w') as fp:
        json.dump(price_dict, fp)



if False:
    ib = IB()
    host = '192.168.0.112'
    #host = '192.168.0.188'
    #local_host = '127.0.0.1'
    ib.connect(host, 8496, clientId=11, timeout=0)

    while(True):
        time_now = dt.datetime.now()
        if time_now.hour > 5 and time_now.hour < 12:
            sys.exit(0)
            
        for symbol in symbols:

            threshold = 0.5
            a_contract = Stock(symbol, 'SMART', 'USD')

            p = price_dict[symbol][0]
            std = price_dict[symbol][1]
            price = latest_price(ib, a_contract)
            
            if p*(1 - threshold*std) > price or price > p*(1+threshold*std):
                pct_change = round(price/price_dict[symbol][0] - 1, 2)
                price_dict[symbol] = Security(price, price_dict[symbol][1])
                
                print(f'{time_now.strftime("%HH:%MM")} {symbol} {price} {100*pct_change}%')
                for i in range(5):
                    
                    winsound.PlaySound('AutoChase.wav',winsound.SND_FILENAME)
                    time.sleep(0.25)
                    
            #print(price)
        ib.sleep(60)

    ib.disconnect()

    