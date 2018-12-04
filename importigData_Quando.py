import quandl

mydata_01 = quandl.get("FRED/GDP")
print(mydata_01.head())
print(mydata_01.tail())

# adatok kiírása csv-be:
import pandas as pd

mydata_01.to_csv('C:/Users/User/Documents/GitHub/Python/csvData/usaGDP.csv')

# adatok behívása csv-ből:
mydata_02 = pd.read_csv('C:/Users/User/Documents/Tozsde/MT4ek/Admiral2/MQL4/Files/csvStatement_27018855/tickBalance.csv')
print(mydata_02.head)
print(mydata_02.tail)

# a beolvasott csv kiírása excellbe:
mydata_02.to_excel('C:/Users/User/Documents/GitHub/Python/csvData/tickBalance.xlsx')



