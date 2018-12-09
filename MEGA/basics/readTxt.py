import os

myfile = open(os.environ['USERPROFILE']+"/Documents/GitHub/Python/MEGA/basics/fruits.txt")
fruits = myfile.read()
myfile.close()
print(fruits)