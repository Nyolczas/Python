import numpy as np

a = np.array([[0,1,2,3],
              [4,5,6,7]])
print(a)
print(a[1,1])
print(a[0,3])

a[1,3]=8

print(a)
print("")

print(a[0])
print(a[1])