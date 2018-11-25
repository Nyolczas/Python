oraber = 3000

def fizu( ora ):
    return ora * oraber

def bonusFizu(ora):
    alap, bonus = 0, 0
    if ora > 9:
         alap = fizu(9)
         oraber = 4500
         bonus = fizu(ora - 9)
         return alap + bonus

    else:
        return fizu(ora)    

print(bonusFizu(10) )         
        
