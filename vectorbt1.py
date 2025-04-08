import vectorbt as vbt

data = vbt.YFData.download(symbols='AAPL', start='2023-01-01', end='2025-02-01').get('Close')


# moving averages
fast_ma = vbt.MA.run(data, window=10)
slow_ma = vbt.MA.run(data, window=50)

# buy and sell conditions
entry_point = fast_ma.ma_crossed_above(slow_ma)
exit_point = fast_ma.ma_crossed_below(slow_ma)

portfolio = vbt.Portfolio.from_signals(data, entries=entry_point, exits=exit_point)

# fig = portfolio.plot()
# fig.show()
print(portfolio.stats())
print()
print(portfolio.total_return())