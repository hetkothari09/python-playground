import pandas as pd
import vectorbt as vbt

start = '2019-01-01 UTC'  # crypto is in UTC
end = '2020-01-01 UTC'

btc_price = vbt.YFData.download('BTC-USD', start=start, end=end).get('Close')
eth_price = vbt.YFData.download('ETH-USD', start=start, end=end).get('Close')

# combined_price = btc_price.vbt.concat('eth_price', keys=pd.Index(['BTC', 'ETH'], name='symbol'))
combined_price = pd.concat([btc_price, eth_price],  axis=1, keys=(['BTC', 'ETH']))
# combined_price.vbt.drop_levels(-1, inplace=True)
combined_price.columns.names=['symbol']
# combined_price = combined_price.astype(float)

fast_ma = vbt.MA.run(combined_price, window=[10, 20])
slow_ma = vbt.MA.run(combined_price, window=[30, 30])

entry_point = fast_ma.ma_crossed_above(slow_ma)
exit_point = fast_ma.ma_crossed_below(slow_ma)

portfolio = vbt.Portfolio.from_signals(combined_price, entry_point, exit_point)

print(portfolio.total_return())

mean_value = portfolio.total_return().groupby('symbol').mean()
fig = mean_value.vbt.barplot(xaxis_title='Mean', yaxis_title='Total value')
fig.show()