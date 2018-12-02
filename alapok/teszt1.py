x = 8
print( "hello" , str(x) + "-as" )
print( "7 is not x:", 7 is not x )
print( "8 is x:", 8 is x)
print( "8.0 is x:", 8.0 is x)
print( "8.0 == x:", 8.0 == x)

def compare_to_8(y):
    if y > 8:   
        return str(y) + " nagyobb, mint 8"
    elif y < 8:   
        return str(y) + " kisebb, mint 8"
    else:
        return str(y) + " annyi, mint 8" 

print(compare_to_8(7))    

lista = [10,20,30,40]
print("max(lista)", max(lista) )
print("min(lista)", min(lista) )
print("sum(lista)", sum(lista) )
print(round(13.276543, 2))

print("lista:", lista )
lista.sort(reverse = True)
print("lista.sort(reverse = True):", lista )


z = -20
print(abs(z))
print(pow(2,12))

# tuples
(years,profit) = "15,200%".split(",")
print(years)
print(profit)