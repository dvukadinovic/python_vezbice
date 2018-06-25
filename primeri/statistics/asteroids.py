"""

Ucitati podatke o ekscentricitetu i inklinaciji malih tela Suncevog sistema i
napraviti raspodelu po datim elementima. Podatke o asteroidima preuzeti iz
baze 'Orbits of Minor Planets' (Bowell 2014) sa Vizier baze podataka. Obratiti
paznju da je data tabela velika, uzeti samo odredjen broj podataka (nekoliko
desetina hiljada) kako ne bi cekali dugo da program ucita podatke.

azurirano: 25. jun 2018.

"""

import numpy as np
import matplotlib.pyplot as plt

i, e = np.loadtxt('asteroids.tsv', unpack=True)
ee = np.sin(e) * 180/np.pi

plt.hist(i, bins=20, histtype='step', range=(-10,50), label='i')
plt.hist(ee, bins=20, histtype='step', range=(-10,50), label='sin(e)')
plt.xlabel(r'$i$ / $\sin (e)$')
plt.ylabel(r'$N$')
plt.legend(loc='best', frameon='False')
plt.show()