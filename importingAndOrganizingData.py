import numpy as np
import pandas as pd

#datalist
ser = pd.Series(np.random.random(5), name = 'Column 01')
print(ser)

#dataframe
from pandas_datareader import data as wb # wb mint web

PG = wb.DataReader('PG', data_source='morningstar', start = '1995-01-01') 
