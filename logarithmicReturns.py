import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')

PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))

PG['log_return'].plot(figsize = (16,9))
plt.show()

avg_returns_d = PG['log_return'].mean() # napi átlag számítása

avg_returns_year = PG['log_return'].mean() * 250 # éves átlag számítása
print('éves átlag hozam (log): ' + str(round(avg_returns_year * 100, 2) ) + ' %')