import os

#myfile = open(os.environ['USERPROFILE']+"/Documents/GitHub/Python/MEGA/basics/fruits.txt")
myfile = open("D:/8I/Code/Python/MEGA/basics/fruits.txt")
content = myfile.read()
myfile.close()

content = content.splitlines()

for i in content:
    print(i +": " + str(len(i)))
