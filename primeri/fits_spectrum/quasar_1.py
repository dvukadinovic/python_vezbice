"""

Radimo sa fits file-ovima. Za to se koristi modul koji se zove 'astropy'. Na
zvanicnoj stranici modula (http://www.astropy.org/) mozete naci sav potreban
materija. Imate sekciju sa tutorialima za koriscenje modula. Nama od trenutnog
interesa je samo rad sa fits file-ovima. Pre nego sto se upustite u ovaj primer
savetujem da predjete preko primera na sajtu: kako se otvaraju fits snimci, sta
se sve sadrzi i kako se barata tim podacima.

U ovom primeru cemo ucitati spektar kvazara i naci talasnu duzinu i fluks u
maksimumu. Spektrlani opseg obuhvata liniju jona CIII] (poluzabranjena
spektralna linija) za koju cemo takodje naci talasnu duzinu na kojoj se javlja
u spektru i izvuci koji je fluks u centru linije. Znamo da se linija javlja u
intervalu 1500-1600 angstrema.

"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# uzimamo samo primarni set podataka (a to je i jedino sto imamo na
# raspolaganju)
hdul = fits.open('kvazar.fits')[0]
# ukoliko fits snimak ima eksteniziju, onda njoj pristupamo tako sto trazimo
# i-ti element hdul-a; npr. za prvu ekstenziju bi stajalo
# 'fits.open('ime_filea.fits')[1]' itd.

# gledamo sta ima u headeru
print(repr(hdul.header))
print()
# Paznja! Ukoliko vam izbaci neke WARNING-e, znamerite ih, nece uticati na
# nas dalji rad

# izvlacimo podatke
flux = hdul.data
# dati podaci sadrze samo fluks na razlicitim talasnim duzinama (koje jos ne
# znamo koje su) u arbitrarnim jedinicama

# pravimo listu talasnih duzina za svaku vrednost fluksa iz header-a fits-a
# imamo dve kljucne reci od interesa: CDELT1 i CRVAL1. Druga kljucna rec nam
# daje referentnu vrednost talasne duzine prvog elementa niza flukseva, dok
# nam prva govori o koraku u talasnim duzinama izmedju susednih podataka.
# Jedinice za talasne duzine su angstremi [\AA].

# preuzimamo vrednosti datih kljucnih reci iz header-a
CDELT1 = hdul.header['CDELT1']
CRVAL1 = hdul.header['CRVAL1']
lamb = np.arange(0, len(flux))*CDELT1 + CRVAL1

# indeks maksimuma zracenja spektra kvazara
ind_max = np.argmax(flux)
# fluks i talasna duzina u maksimumu zracenja
flux_max = flux[ind_max]
lamb_max = lamb[ind_max]
print("Maksimum zracenja kvazara je ", flux_max, " na ", lamb_max, " A \n")

# sada izvlacimo samo fluks od 1500 do 1600 angstrema
aux_flux = flux[ np.where(lamb==1500)[0][0] : np.where(lamb==1600)[0][0] ]
ind_c = np.argmax(aux_flux)
flux_c = aux_flux[ind_c]
lamb_c = lamb[flux==flux_c][0]

print("Fluks u CIII] liniji u spektru kvazara je ", flux_c, ", a ilinija je na \
", lamb_c, " A \n")

plt.plot(lamb, flux, lw=0.75)
plt.plot([lamb_c, lamb_c], [flux_c*1.1, flux_c*1.5], 'k-', lw=0.75)
plt.xlabel(r'$\lambda [\AA]$')
plt.ylabel(r'$F [AU]$')
plt.text(lamb_c-200, flux_c*1.6, 'CIII]')
plt.show()