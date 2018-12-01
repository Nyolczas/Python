import math

print(math.sqrt(16))

# lehet úgy is hogy csak azt az adott osztályt hívom be a modulból amire épp szüségem van:
from math import sqrt

print(math.sqrt(25))

# időtakarékos módszer, ha egyből példányosítom az osztályt:
from math import sqrt as s

print(s(36))

# mégegy módszer:
import math as m

print(m.sqrt(49))

# ... és mégegy:
#from math import * # ez minden osztályt behív a modulból

print(sqrt(64))

help(math.sqrt)


