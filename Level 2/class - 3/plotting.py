import numpy as np
import matplotlib.pyplot as plt

temps = [1, 2, 3, 4, 5, 6, 7, 8, 9]

temperature = [5.5, 7.2, 8.5, 11.6, 13.6, 18.8, 21.5, 22.5, 25.8]

plt.scatter(temps, temperature, marker="o", color="blue")

plt.xlabel("Temp in hours")
plt.ylabel("Temperature in Celcius")
plt.title("Temperature progression per hour")
x = np.linspace(min(temps), max(temps), 50)
print(x)

y = 2 + 3 * x
print(y)

plt.plot(x, y, color="green", ls="--")

plt.grid()
# plt.savefig("graphic.png", bbox_inches="tight", dpi=200)
plt.show()
