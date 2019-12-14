import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

a = [1, 2, 3, 4]
print(a)
print(type(a))

b = np.array(a)
print(b)
print(type(b))

c = np.arange(10)
print(c)

d = np.arange(10.0)
print(d)

v = np.arange(4)
print(v)

v = v + 1
print(v)
v = v + 0.1
print(v)
v = v * 2
print(v)

v = v * v
print(v)

w = np.array([[1, 2], [3, 4], [5, 6]])
print(w)

z = np.arange(4)
print(z)
print(z.ndim)
print(w.ndim)

print(z.shape)
print(w.shape)

print(z.size)
print(w.size)

a = np.arange(10)
print(a)

a.resize(3, 3)
print(a)

a = np.zeros((2, 3))
print(a)

b = np.zeros((2, 3), int)
print(b)

c = np.zeros(5)
print(c)

d = np.zeros(5, int)
print(d)

e = np.ones((2, 3), int)
print(e)

f = np.ones(5, int)
print(f)

g = np.full((2, 3), 5, float)
print(g)

g = np.full(7, 2, float)
print(g)

c = np.arange(1, 10)
print(c)
a = np.resize(c, (3, 3))
print(a)

d = np.transpose(a)
print(d)

temps = [1, 2, 3, 4, 5, 6, 7, 8, 9]

temperatures = [5.5, 7.2, 8.5, 11.8, 13.6, 18.8, 21.5, 22.5, 25.8]
plt.scatter(temps, temperatures, marker="o", color="blue")

plt.xlabel("Temps en heure")
plt.ylabel("Temperature en degre")

plt.title("Progression de la Temperature par heure")

x = np.linspace(min(temps), max(temps), 50)

print(x)

y = 2 + 3 * x
print(y)

plt.plot(x, y, color="green", ls="--")

plt.grid()

# plt.show()

plt.savefig("grafique.png", bbox_inches="tight", dpi=200)

df = pd.DataFrame(columns=["c1", "c2", "c3", "c4"],
                  index=["L1", "L2", "L3"],
                  data=[np.arange(10, 14),
                        np.arange(20, 24),
                        np.arange(30, 34)])
print(df.shape)
print(df.columns)
print(df.head((2)))
print(df[["c1", "c2"]])
print(df.info())
