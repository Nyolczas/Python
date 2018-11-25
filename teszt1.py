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