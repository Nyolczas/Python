import quandl

mydata_01 = quandl.get("FRED/GDP")
print(mydata_01.tail())