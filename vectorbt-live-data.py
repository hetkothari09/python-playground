import time

import vectorbt as vbt
import ccxt
import time

# exchange = cctx.binance()
# data = vbt.CCXTData.fetch('binance', 'BTC/USDT', timeframe='1m', limit=100)
# print(data.tail())
# import ccxt

# Initialize Binance exchange
exchange = ccxt.binance()


while True:

    # Fetch latest ticker data for BTC/USDT
    ticker = exchange.fetch_ticker('BTC/USDT')

    # Print live price
    time.sleep(1)
    print(f"BTC/USDT Live Price: {ticker['last']}")

