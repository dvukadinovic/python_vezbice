"""

U fajlu 'radio' dati su posmatracki podaci ostatka supernove Cas A. U prvoj
koloni je frekvenca posmatranja u GHz, zatim gustina fluksa i greska gustine
fluksa u Jy.

Zadatak je da se na dati spektar zracenja fituje model zracenja stepenim
zakonom. Na kraju ispisati vrednosti parametera fita.

"""

import numpy as np
import matplotlib.pyplot as plt
# ucitavamo funkciju 'curve_fit' pomocu koje cemo fitovati data posmatranja
from scipy.optimize import curve_fit

freq, Snu, dSnu = np.loadtxt('radio', unpack=True)

# sada definisemo funkciju kojom cemo fitovati prvi parametar je nezavisna
# promenljiva, a ostali su parametri funkcije kojom fitujemo
def fit_fun(x, S0, alfa):
	y = S0 * x**(-alfa)
	return y

# fitujemo! obavezno se sledecim redom navode stvari kada koristimo
# 'curve_fit': 1. funkcija kojom se fituje 2. nezavisna promenljiva 3. zavisna
# promenljiva Ako imate i greske onda se dodaje kljucna rec 'sigma' i
# prosledjuje niz koji sadrzi greske merenja.
par, cov = curve_fit(fit_fun, freq, Snu, sigma=dSnu)
# par: lista koja sadrzi najoptimalnije vrednosti parametara; cov: kovarijantna
# matrica; dijagonalni elementi sadrze varijanse datih parametara

# Takodje se mogu zadati pocetne vrednosti parametara iz kojih ce algoritam da
# krene da trazi optimalne parametre. Kljucna rec je 'p0' i pocetne vrednosti
# se navode kao lista (primer ispod)
# par, cov = curve_fit(fit_fun, freq, Snu, sigma = dSnu, p0 = [150,0.7])

print(*par)

# sada cemo vizuelno da proverimo koliko dobro je uradjen fit

plt.errorbar(np.log10(freq), np.log10(Snu), yerr=dSnu/Snu/np.log(10), 
			c='k', ms=4, fmt='o', label='posmatranja')
plt.plot(np.log10(freq), np.log10(fit_fun(freq, *par)), 'r-', label='fit')
plt.xlabel(r'$\log (\nu)$ $[$GHz$]$')
plt.ylabel(r'$\log (S_\nu)$ $[$Jy$]$')
plt.text(0, 2.5, 'Cas A')
tekst = r'$\alpha=$' \
		+ r'${:5.4f}$'.format(par[1]) \
		+ r'$\pm$' + r'${:5.4f}$'.format(cov[1,1])
plt.text(0, 2, tekst)
plt.legend(frameon=False, loc='best')
plt.savefig('snr_spectrum.png')
plt.show()