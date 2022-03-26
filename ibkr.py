
from ib_insync import *
util.patchAsyncio()


port = 8496
ib = IB()
ib.connect('127.0.0.1', port, clientId=15)



symbols = ['BABA', 'WMT', 'SNOW', 'COIN']

contracts = [Stock(symbol, 'SMART', 'USD') for symbol in symbols]

ib.qualifyContracts(*contracts)


for contract in contracts:
    ib.reqMktData(contract, '', False, False)

ib.disconnect()