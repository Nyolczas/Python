import quandl

mydata_01 = quandl.get("FRED/GDP")
print(mydata_01.head())
print(mydata_01.tail())

# adatok kiírása csv-be:
import pandas as pd
import os
mydata_01.to_csv(os.environ['USERPROFILE']+'/Documents/GitHub/Python/csvData/usaGDP.csv')

# adatok behívása csv-ből:
mydata_02 = pd.read_csv(os.environ['USERPROFILE']+'/Documents/Tozsde/MT4ek/Admiral2/MQL4/Files/csvStatement_27018855/tickBalance.csv')
print(mydata_02.head)
print(mydata_02.tail)

# a beolvasott csv kiírása excellbe:
mydata_02.to_excel(os.environ['USERPROFILE']+'/Documents/GitHub/Python/csvData/tickBalance.xlsx')

#lehagyja a beolvasásból az alapértelmezett sorszámozást és az indexelő oszlop a megadott oszlop lesz 
mydata_03 = pd.read_csv(os.environ['USERPROFILE']+'/Documents/GitHub/Python/csvData/Data_02.csv', index_col='Date')
print(mydata_03)

#excel beolvasása
mydata_04 = pd.read_excel(os.environ['USERPROFILE']+'/Documents/GitHub/Python/csvData/Data_03.xlsx')
print(mydata_04)
mydata_04 = mydata_04.set_index('Year') #utólag indexeli a behívott adatokat a Year oszloppal
print(mydata_04)
