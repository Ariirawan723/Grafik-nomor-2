import numpy as np

import matplotlib.pyplot as plt

def H(y):

  return 0.725 * (((960 ** 2) * (9.8) * (2.255 * 10 ** 6) * (0.68 ** 3) / ((20) * (y) * (2.82 * 10 ** -4) * (3))) ** 0.25)

def Massa(x):

  return x / 3600

def Q2(x):

  return x * 2.255 * 10 ** 6

def L(x, y):

  return round(x / (y * 400 * 3.14 * 3 * 0.01),2)

varMas = [550, 600, 635, 675, 700]

varD = [0.01, 0.05, 0.08, 0.1, 0.12]

la = []

li = []

for i in range(len(varMas)):

  la.append(L(Q2(Massa(varMas[i])), H(0.01)))

for j in range(len(varD)):

  li.append(L(Q2(Massa(600)), H(varD[j])))

x = [1, 2, 3, 4, 5]

plt.plot(x, la, marker="o", label="variasi Massa")

plt.plot(x, li, marker="o", label="variasi diameter tabung")

plt.ylabel("Panjang Tabung (m)")

plt.title("Grafik Panjang Tabung")

plt.legend()

plt.grid()

plt.show()

print(f"Hasil dari variasi Massa = {la}")

print (f"Hasil dari variasi diamater tabung = {li}")
