# megszámolja az adott listában, hogy hány elemnek kissebb az értéke a megadottnál
def count(numbers, maxValue):
    total = 0
    for x in numbers:
        if x < maxValue:
            total += 1
    return total

list_1 = [1,3,5,47,51,89,12,14,85]   

print(count(list_1, 8))         
print(count(list_1, 20))         
print(count(list_1, 88))         