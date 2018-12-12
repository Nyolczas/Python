import os
from datetime import datetime

path = os.environ['USERPROFILE']+'/Documents/GitHub/Python/MEGA/beyondBasics/'
filenames = [path + 'file1.txt', path + 'file2.txt', path + 'file3.txt']
with open(path + datetime.now().strftime("%Y.%m.%d %H-%M-%S") + ".txt", 'w') as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read() + "\n")