import os

myfile = open(os.environ['USERPROFILE']+"/Documents/GitHub/Python/MEGA/basics/fruits.txt")
fruits = myfile.read()
myfile.close()

print(fruits)
print(type(fruits))
print(len(fruits))
print(fruits[0])

fruits.splitlines()
print(fruits)
print(type(fruits))
print(len(fruits))
print(fruits[0])
