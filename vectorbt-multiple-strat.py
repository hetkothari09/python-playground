import vectorbt as vbt
import pandas as pd

start = '2020-01-01'
end = '2025-01-01'

aapl_data = vbt.YFData.download('AAPL', start=start, end=end).get('Close')
mrf_price = vbt.YFData.download('MRF', start=start, end=end).get('Close')

concat_price = pd.concat([aapl_data, mrf_price], keys=['AAPL', 'MRF'], axis=1)
# concat_price.vbt.drop_level(-1, inplace=True)

'''
creates 2 instances of strategies. 1 with 10 and 30 and other with 20 and 30. 
'''
fast_ma = vbt.MA.run(aapl_data, [10, 20], short_name='fast')
slow_ma = vbt.MA.run(aapl_data, [30, 30], short_name='slow')

entry_point = fast_ma.ma_crossed_above(slow_ma)
exit_point = fast_ma.ma_crossed_below(slow_ma)

# portfolio = vbt.Portfolio.from_signals(aapl_data, entries=entry_point, exits=exit_point)
portfolio = vbt.Portfolio.from_signals(concat_price, entries=entry_point, exits=entry_point)
print(portfolio.total_return())
# print(portfolio.stats())
