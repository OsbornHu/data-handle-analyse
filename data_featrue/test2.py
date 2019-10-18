
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl

import datetime
import pandas as pd
import pandas_datareader.data as web

from pandas import Series, DataFrame
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 1, 11)
df = web.DataReader("AAPL", 'yahoo', start, end)
#print(df.tail())

close_px = df['Adj Close']
rets = close_px / close_px.shift(1) - 1
rets.plot(label='return')
plt.legend()
plt.show()