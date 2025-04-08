import vectorbt as vbt

stocks = ['AAPL', 'TSLA', 'MSFT']

data = vbt.YFData.download(stocks, start='2020-01-01').get('Close')

portfolio = vbt.Portfolio.from_holding(data, init_cash=10000)

# portfolio.plot().show()
# fig = portfolio.plot(column='AAPL')
# fig2 = portfolio.plot(column='TSLA')
# fig3 = portfolio.plot(column='MSFT')
# fig.show()
# fig2.show()
# fig3.show()

risk_ratio = portfolio.returns_acc.sharpe_ratio()
print(risk_ratio)