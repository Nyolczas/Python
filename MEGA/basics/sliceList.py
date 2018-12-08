myList = ["béka", "csöcs", 112]

print(myList[0:2])
print(myList[1:2])
print(myList[1])
print(myList[:2])
print(myList[-2:])


napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]

print(napok[0:5])
print(napok[4])
print(napok[4:6])
print(napok[6])

myList.remove(112)
print(myList)

myList.append("szopogatás")
print(myList)

myList.pop(1)
print(myList)

napok.sort()
print(napok)


