import os

#myfile = open(os.environ['USERPROFILE']+"/Documents/GitHub/Python/MEGA/basics/fruits.txt")
myfile = open("D:/8I/Code/Python/MEGA/basics/fruits.txt")
fruits = myfile.read()
myfile.close()

fruits = fruits.splitlines()

for i in fruits:
    print(i +": " + str(len(i)))
