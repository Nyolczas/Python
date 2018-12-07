import numpy as np
import pandas as pd

#datalist
ser = pd.Series(np.random.random(5), name = 'Column 01')
print(ser)

#dataframe PG
from pandas_datareader import data as wb # wb mint web

PG = wb.DataReader('PG', data_source='iex', start = '2014-01-01') # iex mellett morningstar-ral is lehet próbálkozni 

print(PG)

# több instrumentum lehívása
tickers = ['PG', 'MSFT', 'T', 'F', 'GE']
new_Data = pd.DataFrame()
for t in tickers:
    new_Data[t] = wb.DataReader(t, data_source='iex', start='2014-01-01')['close']

print(new_Data.tail())  
