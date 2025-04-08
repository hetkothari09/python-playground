import vectorbt as vbt

start = '2019-01-01'
end = '2020-01-01'

data = vbt.YFData.download('AAPL', start=start, end=end).get('Close')

rsi = vbt.RSI.run(data, window=14)

entry_point = rsi.rsi_crossed_below(30)
exit_point = rsi.rsi_crossed_above(70)

portfolio = vbt.Portfolio.from_signals(data, entry_point, exit_point)

print(portfolio.total_return())

# 045391188863180075