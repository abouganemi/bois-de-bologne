import numpy as np

a = np.arange(10)
print(a)

a.resize(3, 3)
print(a)

a = np.zeros((2,3))
print(a)

b = np.zeros((2, 3), int)
print(b)

c = np.zeros((5))
print(c)

d = np.zeros((5), dtype=int)
print(d)

e = np.ones((2, 3), dtype=int)
print(e)

f = np.ones((5), dtype=int)
print(f)
