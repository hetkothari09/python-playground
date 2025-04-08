import ccxt
import vectorbt as vbt

exchange = ccxt.binance()

order_book = exchange.fetch_order_book('BTC/USDT')
print("Top 5 bids: ", order_book['bids'][:5])
print("Top 5 Asks: ", order_book['asks'][:5])


trades = exchange.fetch_trades('BTC/USDT')
print("Last 5 trades: ", trades[:5])