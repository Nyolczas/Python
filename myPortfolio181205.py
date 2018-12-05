import pandas as pd
from pandas_datareader import data as wb # wb mint web

# portfolio instrumentum lehívása
tickers = ['BTMA.AS', 'DAXEX.SW', 'SXRV.DE', 'SXR8.DE'] # csak az első 3 az, a bux nincs benne
new_Data = pd.DataFrame()
for t in tickers:
    new_Data[t] = wb.DataReader(t, data_source='yahoo', start='2013-10-01')['Adj Close']

print(new_Data.tail())  