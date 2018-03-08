"""
Skripta broj 5.

Rad sa modulima - scipy

Mouli sadrze skup razlicitih funkcija koje se pozivaju u formatu:
naziv_modula.ime_funkcije(objekat_na_koji_primenjujemo_funckiju)

Scipy modul sadrzi operacije nad numericim nizovima (type je ndarray) kao
sto su interpolacija, integracija, optimizacija (fitovanje) i mnoge
druge. Scipy modul je namenjen za rad u okviru naucne zajednice.

23. februar 2018.
"""

import numpy as np 									# vec vidite da se nista ne moze bez numpy
import matplotlib.pyplot as plt						# i matplotlib modula
from scipy.integrate import simps 					# funkcija koja racuna integral primenom
													# Simpsonove integralne seme
from scipy.interpolate import interp1d				# funkcija za 1D interpolaciju
from scipy.optimize import curve_fit				# funkcija kojom se fituje

a, b, c = np.loadtxt('test_podaci', unpack = True)

#===================================================#

print ('Integral je: ', simps(b, a))				# prvi argument je 'y'; opcino se moze dodati
													# i vrednosti 'x', ako se ne daju, funkcija
													# podrazumeva da je razmak izmedju tacaka 1

#===================================================#

intpfun = interp1d(a, b)							# napravili smo interpolacionu funkciju na osnovu
													# izmerenih vredonsti a i b
print ('Vrednost funkcije u x=3.5 je ', 			# trazimo vrednost u tacki x = 3.5
		intpfun(3.5))

#===================================================#

def fitfun(x, a0, a1, a2):
	"""
	definisemo kvadratnu funkciju kojom cemo
	fitovati ucitane podatke.

	Funkcija kojom fitujemo obavezno na prvom
	mestu ima nezavisnu promenljivu 'x', a ostali
	argumenti su nepoznati koeficijenti funkcije
	koje zelimo da dobijemo fitovanjem.
	"""
	rez = a2 * x**2 + a1 * x + a0
	return rez

par, cov = curve_fit(fitfun, a, b, sigma = c)		# opciono je davanje gresaka merenja preko argumenta
													# 'sigma'; izlaz iz fita su 2 promenljive:
													#  	- par : niz najboljih vrednosti za nepoznate 
													#			koeficijente funkcije (kako su naredjani
													#			u funkciji tako su i u nizu)
													#	- cov : kovarijantna matrica (na dijagonali su
													# 			varijanse datih koeficijenata)

x = np.linspace(min(a), max(a), num = 31)
plt.errorbar(a, b, c, fmt = 'o', 
					  label = 'posmatranja')		# crtamo najbolji fit kako bismo uporedili sa
plt.plot(x, fitfun(x, par[0], par[1], par[2]),		# posmatranjima
					  label = 'najbolji fit')		# jednostavniji poziv fitfun je: fitfun(x, *par)
													# *par - kada je 'par' niz, podelice ga sam u pojedinacne
													# 		 elemente i proslediti funkciji
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 2, frameon = False)
plt.savefig('najbolji_fit.png')