import numpy as np
import matplotlib.pyplot as plt

array = [1,2,3,5,5,6,7]

for i in range(len(array)):
    print(array[i])

def test(x, y):
    z = x**y
    w = x+y
    return z,y

s = test(2,5)
print(s)

list = [1,2,3,4,1,2,2,3,8,9,2,100, -10]

z = np.sort(list)
range = z[-1] - z[0]
print(range)
print(z)

w = 0.8
print(round(w))

for i in len(range(19)):
    print(i)
