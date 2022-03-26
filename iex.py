import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data

import pandas as pd
import requests
from termcolor import colored as cl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (15,8)

from iexfinance.stocks import Stock
from iexfinance.refdata import get_symbols
import os

#IEX_TOKEN  = 'pk_6fe43330db534b2ea88042a08674dd03'
IEX_TOKEN = 'pk_23221a9345a345d085039da077b6c4a2'
from iexfinance.refdata import get_symbols


os.environ["IEX_TOKEN"] = IEX_TOKEN
os.environ['IEX_SANDBOX'] = 'enable'

if __name__ == "__main__":
    #get_symbols(token=IEX_TOKEN)
    batch = Stock(["TSLA", "AAPL"])
    batch = Stock('AAPL')
    print(batch.get_price())
    #print(batch.get_quote())










import pip
import pandas as pd

import yfinance as yf




tsla_df = yf.download('TSLA',
                      start='2021-01-01',
                      end='2021-12-31',
                      progress=False)

print(tsla_df["Close"].iloc[-1])



    api_url = f'https://api.iextrading.com/1.0/tops/last?symbols='
    for s in symbols:
        api_url = api_url + f'{s},'
    print(api_url)
    list = requests.get(api_url).json()

    price_latest = {}



    for item in list:
        print(item)
        price_latest[item['symbol']] = item['price']

        #print(item['symbol'], item['price'])
