"""

Program koji racuna ekvivalentu sirinu spektralne linije. Podaci o spektralnoj
liniji se nalaze u fajlu "linija.txt".

Ekvivalena sirina predstavlja meru jacine linije i predstavlja povrsinu linije.
Odnosno, to je sirina pravougaonika cija je visina normirana na kontinuum, a
povrsina pravougaonika odgovara povrsini linije.

azurirano: 14. april 2018.
"""

import numpy as np
import matplotlib.pyplot as plt

lam, Int = np.loadtxt('linija.txt', unpack=True)

# racunamo odstupanje intenziteta za svaku talasnu duzinu od kontinuuma
y = 1-Int

# nalazimo centralnu talasnu duzinu spektralne linije 
lam0 = lam[np.argmin(Int)]

# ===--- trapezoidna integracija ---=== #
EW = 0
for ii in range(1,len(lam)):
	EW += (lam[ii] - lam[ii-1]) * (y[ii] + y[ii-1]) / 2

print("EW: ", EW, " A \n")

def nearestarg(br, niz):
	"""
	Funkcija koja vraca indeks elementa u nizu koji je najblizi datom broju
	"""
	ind = np.argmin(abs(niz - br))
	return ind

# pozivamo funkciju koja nam vraca indekse granice pravougaonika
# obratite paznju da funkciju mozemo pozvati na dva razlicita nacina
ind1 = nearestarg(lam0 - EW/2, lam)
ind2 = nearestarg(br=lam0 + EW/2, niz=lam)

# crtamo spektralnu liniju
plt.plot(lam, Int, color = 'black')
# crtamo kontinuum
plt.plot(lam, np.ones(len(lam)), 'k--', linewidth=0.75)
# teskt mozemo i navoditi u LaTeX stilu, ali stringu mora da prethodni $ oznaka
plt.xlabel(r'$\lambda\ [\AA]$')
plt.ylabel(r'$I/I_c$')
# y granice plota
plt.ylim([0, 1.1])
# srafiramo grafik tako da pravimo pravougaonik cija je povrsina jednaka
# povrsini linije
plt.fill_between(lam[ind1:ind2+1], 0, 1, color='orange', alpha=0.25)
# ispisujemo ekvivalentnu sirinu na grafik
# x pozicija na 25% rastojanja od leve ivice do centra linije
xpos = 0.25 * (lam0-lam[0]) + lam[0]
ypos = 0.4
# formatiramo ispis tako da bude tipa float i da ima broj od 7 mesta, a 5 broja
# iza tacke; vise o formatiranju ispisa na: https://pyformat.info/
tekst = r'$W=$' + r'${:7.5f}$'.format(EW) + r' $\AA$'
plt.text(xpos, ypos, tekst)
plt.savefig('ew_plot.png', dpi=90)
plt.show()

"""

Koristeci vec gotove funkcije u Pythonu mozemo na mnogo jednostavniji nacin da
izracunamo ekvivalentnu sirinu linije. Za to korisimo funkciju 'simps' iz scipy
paketa.

"""

from scipy.integrate import simps

EW = simps(y, lam)

print("EW (simps): ", EW, " A \n")
# prakticno dobijate istu ekvivalentu sirinu linije, sto je i ocekivano ako ste
# napisali lepo integracionu semu
