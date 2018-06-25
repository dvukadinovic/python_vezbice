"""

Dat je 2D spektar Sunca. Prva dimenzija odgovara poziciji na povrsini Sunca
(spektar se prostire od ruba do centra), dok druga dimenzija odgovara talasnim
duzinama.

Potrebno je izdvojiti liniju stroncijuma (izmedju 140. i 160. kolone) i
graficki predstaviti promenu intenziteta u centru linije sa udaljenoscu od
ruba diska Sunca. Proveriti kako izgleda ceo spektar za nelikoliko razlicitih
udaljenosti od ruba.

azurirano: 25. jun 2018.
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

hdu = fits.open('solar.fits')[0]
spectrum = hdu.data

# 2D spektar
plt.imshow(spectrum)
plt.colorbar()
plt.show()

print(repr(hdu.header), '\n')

# spektar na proizvoljnom rastojanju od
plt.plot(spectrum[120,:])
plt.xlabel(r'$x$')
plt.ylabel(r'$F[AU]$')
plt.show()

# izvlacimo samo liniju Sr
data_sr = spectrum[2:-2, 140:161]
# Paznja! Dimenzije ucitanih podataka nisu istog rasporeda kao sto je
# predstavljeno u headeru. Python je zamenio dimenzije

sr_ind_min = np.argmin(data_sr, axis=1)
sr_min = [data_sr[ii, sr_ind_min[ii]] for ii in range(len(sr_ind_min))]

plt.plot(sr_min)
plt.xlabel(r'$x$')
plt.ylabel(r'$F[AU]$')
plt.show()