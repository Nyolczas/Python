a = ['a', 'b', 'c']
b = [1, 2, 3]

for i, j in zip(a, b):
    print("%s is %s" %(i, j)) # string formatted version

for i, j in zip(a, b):
    print(i, j) # simple version