import vectorbt as vbt
import pandas as pd


start = '2019-01-01 UTC'
end = '2020-01-01 UTC'

btc_price = vbt.YFData.download('BTC-USD', start=start, end=end).get('Close')
eth_price = vbt.YFData.download('ETH-USD', start=start, end=end).get('Close')

combined_prices = pd.concat([btc_price, eth_price], axis=1, keys=['UTC', 'ETH'])

combined_prices.columns.names = ['symbol']

'''
This splits the time interval into 2 parts and tests the strategy in both time intervals
_ is called a throwaway variable, it is used when you dont want to use a value of that variable
if i had assigned that variable it would give me time-range values which is not required (2019-01-01 - 2019-06-30, 2019-07-01 - 2019-12-31)
'''

multi_col_combined, _ = combined_prices.vbt.range_split(n=2)

fast_ma = vbt.MA.run(multi_col_combined, [10, 20])
slow_ma = vbt.MA.run(multi_col_combined, [30, 30])

entry_point = fast_ma.ma_crossed_above(slow_ma)
exit_point = fast_ma.ma_crossed_below(slow_ma)

# portfolio = vbt.Portfolio.from_signals(multi_col_combined, entry_point, exit_point)
portfolio = vbt.Portfolio.from_signals(multi_col_combined, entry_point, exit_point, freq='1D')

print(portfolio.total_return())

mean_price = portfolio.total_return().groupby(['split_idx', 'symbol']).mean()
fig = mean_price.unstack(level=-1).vbt.barplot(
    xaxis_title='split index',
    yaxis_title='total mean value',
    legend_title_text='symbol'
)

fig.show()