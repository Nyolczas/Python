import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
print(PG.head())
print(PG.tail())

#line chart
PG['Adj Close'].plot(figsize=(16,9))
plt.show()

#napi %-os hozam számítása:
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1))-1
print(PG['simple_return'])

PG['simple_return'].plot(figsize=(16,9))
plt.show()

avg_returns_d = PG['simple_return'].mean() # átlag számítása

avg_returns_year = PG['simple_return'].mean() * 250
print('éves átlag hozam: ' + str(round(avg_returns_year * 100, 2) ) + ' %')