"""

Radimo sa fits file-ovima. Za to se koristi modul koji se zove 'astropy'. Na
zvanicnoj stranici modula (http://www.astropy.org/) mozete naci sav potreban
materija. Imate sekciju sa tutorialima za koriscenje modula. Nama od trenutnog
interesa je samo rad sa fits file-ovima. Pre nego sto se upustite u ovaj primer
savetujem da predjete preko primera na sajtu: kako se otvaraju fits snimci, sta
se sve sadrzi i kako se barata tim podacima.

Potrebno je izdvojici deo spektra oko linije CIII] koja se nalazi na 1909 \AA
i fitovati kontinuum oko linije. Za kontinuum uzeti podatke iz intervala
1800-1820 i 2020-2040 \AA. Takodje, napraviti subplot gde ce na jednom grafiku
biti linija sa fitom kontinuuma dok je na drugom normalizovani spektar. Na
kraju je potrebno izdvojeni normalizovani spektar linije sacuvati u fits file
(ne zaboravite da korigujete shodno i header snimka koji cuvate!).

azurirano: 25. jun 2018.

"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy.optimize import curve_fit

hdul = fits.open('kvazar.fits')[0]
head = hdul.header
flux = hdul.data

CDELT1 = hdul.header['CDELT1']
CRVAL1 = hdul.header['CRVAL1']
lamb = np.arange(0, len(flux))*CDELT1 + CRVAL1

# izvlacimo samo fluks koji nas interesuje (od 1800 do 2000 \AA).
flux = flux[ np.where(lamb==1800)[0][0] : np.where(lamb==2040)[0][0] ]
lamb = np.arange(1800, 2040, 0.5)

# izvlacimo samo kontinuum
flux_cont = np.hstack((flux[lamb<1820],flux[lamb>2020]))
lamb_cont = np.hstack((lamb[lamb<1820],lamb[lamb>2020]))

def lin_fun(x, a, b):
	return a*x + b

par,_ = curve_fit(lin_fun, lamb_cont, flux_cont)
# ako vas neki od parametera koje vraca funkcija ne znamia, onda umesto da
# dedelite tu vrednost nekoj promenljivoj mozete samo umesto nje staviti znak
# '_', kao gore sto stoji

flux_norm = (flux / lin_fun(lamb, *par))

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(lamb, flux, 'k-', lw=0.75)
ax1.plot(lamb, lin_fun(lamb, *par), 'k--', lw=0.75, label='Kontinuum')
ax1.set_ylabel(r'$F [AU]$')
ax1.text(1950, 1.2, 'CIII]')
ax1.legend(loc='best', frameon=False)

ax2.plot(lamb, flux_norm, 'k-', lw=0.75)
ax2.plot([min(lamb),max(lamb)], [1,1], 'k--', lw=0.75, label='Kontinuum')
ax2.set_ylabel(r'$F/F_c$')
ax2.set_xlabel(r'$\lambda [\AA]$')
ax2.text(1950, 1.5, 'CIII]')
ax2.legend(loc='best', frameon=False)

plt.savefig('norm_spectrum.png', dpi=90)
plt.show()
# Napomena! Kada se radi sa subplotom svi argumenti (osim plota) treba da
# krenu sa slogom 'set_' da bi se izvrsila linija kod i prikazalo na plotu
# kasnije

# ispisivanje podatkaa u novi fits file; prvo setujemo novi objekat koji ce
# sadrzati nase podatke i header file; potom dodeljujemo vrednosti podacima
# ('data') i samom headeru; u headeru mozemo da dodajemo nove kljucne reci
# samo zadajuci vrednost toj kljucnoj reci (kao sto dole stoji; pre toga hdu u
# headeru nije imao 'CRVAL1')

hdu = fits.PrimaryHDU()
hdu.data = flux_norm
hdu.header['CRVAL1'] = 1800
hdu.header['CDELT1'] = 0.5
hdu.header['SOFTWARE'] = 'Python3 Astropy module'
hdu.header['COMMENTS'] = 'Evo ovako se radi sa fits file-ovima! :)'

hdul = fits.HDUList(hdu)
hdul.writeto('norm_kvazar.fits', overwrite=True)