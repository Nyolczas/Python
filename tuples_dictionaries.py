def negyzet_info(x):
    terulet = x ** 2
    kerulet = x * 4
    return terulet,kerulet

print(negyzet_info(12))    #tuple-t ad vissza

# dictionary:
dict = {"openTime" : "2018.10.24", "closeTime" : "2018.10.28", "profit" : 25.42}
print(dict["profit"])

dict["profit%"] = "3.21%"

print(dict)

# dictionary másképp definiálva:
PriceData = {}
PriceData['Date'] = '2018.11.23.'
PriceData['Open'] = 256.54
PriceData['High'] = 258.14
PriceData['Low']  = 252.03
PriceData['Close'] = 257.99

print(PriceData)