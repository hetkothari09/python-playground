from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import GOOG, SMA


class SMACross(Strategy):
    short_range = 10
    long_range = 20

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.short_range)
        self.sma2 = self.I(SMA, self.data.Close, self.long_range)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

strategy = Backtest(GOOG, SMACross, cash=100000, commission=0.0002)
stats = strategy.run()
# fig = strategy.plot()
# fig.show()
print(stats)