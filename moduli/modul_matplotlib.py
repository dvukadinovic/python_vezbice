"""
Skripta broj 4.

Rad sa modulima - matplotlib

Mouli sadrze skup razlicitih funkcija koje se pozivaju u formatu:
naziv_modula.ime_funkcije(objekat_na_koji_primenjujemo_funckiju)

Matplotlib modul sadrzi funkcije uz pomoc kojih se crtaju razni grafici,
prave animacije i slicno. Mnogi primeri kako se koristi modul se mogu
naci na: https://matplotlib.org/gallery/index.html.

23. februar 2018.
"""
import numpy as np
import matplotlib.pyplot as plt 				# importujemo modul za grafiku, skraceno kao 'plt'

a, b, c = np.loadtxt('test_podaci', unpack = True)

#===============================================#

plt.plot(a,b)									# obican plot podataka (tacke su spojene linijama i to 
plt.show()										# redom kao sto su date u nizovima 'a' i 'b'

#===============================================#

plt.errorbar(a, b, c, fmt = 'o')				# plot tacaka sa greskama gde su tacke predstavljene
plt.show()										# karakterom 'o'

#===============================================#

plt.scatter(a, b, c = 'black', s = 10, 			# funkcija koja crta crne tacke velicine 10
				  label = 'kvadratna funkcija')	# mozemo prelomiti i liniju u drugi red ako je predugacka
plt.xlabel('ime x ose [dimenzija]')
plt.ylabel('ime y ose [dimenzija]')
plt.xticks(np.arange(min(a), max(a), 0.5))		# oznake na x osi
plt.legend(loc = 'best', frameon = False)		# crtamo legendu (ima smisla samo ako plot ima 'label')
plt.show()

#===============================================#

a = np.random.normal(5, 1, 2000)
plt.hist(a, bins = 20)							# histogram sa 20 binova
plt.text(2, 250, 'histogram')					# mozemo da pisemo po grafiku - prva dva broja su koordinate
plt.show()										# sa kojih pocinje tekst - (x,y) par

#===============================================#

x = np.linspace(0, 3*np.pi, 51)
plt.plot(x, np.sin(x), color = 'red')			# mozemo da crtamo vise plotova na jedan grafik
plt.plot(x, np.sin(x + 0.25), color = 'magenta')# Python ce sve plotove da smesti na jedan grafik
plt.show()										# sve dok mi ne prikazemo taj grafik

#===============================================#

plt.figure()									# inicijalizujemo grafik

plt.subplot(121)								# pravimo dva plota na jedan grafik i to sa 1 redom i 2 kolone
plt.plot(x, np.sin(x))							# crtamo 1. (zato je 121) - prva 2 broja govore o rasporedu
												# plotova, a poslednji broj o rednom broju plota koji crtamo

plt.subplot(122)								
plt.plot(x, np.cos(x))							# crtamo 2. (zato je 122)

plt.show()

#===============================================#

fig, ax = plt.subplots(1, 2, sharey = True)		# drugaciji pristup definisanju vise plota na jedan grafik;
												# 'ax' sadrzi lisu plotova - ax[0] je prvi, a ax[1] je drugi;
												# sharey = True - plotovi dele zajednicku y-osu - ne ponavljaju
												# 				  se vrednosti na y osi na drugom grafiku

ax[0].plot(x, np.sin(x), color = 'red', 
						 label = 'sinusna funkcija')
ax[1].plot(x, np.cos(x), color = 'black',
						 label = 'kosinusna funkcija')

fig.legend(loc = 'best')
plt.savefig('subplot_sharey.png', dpi = 90)		# cuvamo grafik sa rezolucijom 90dpi; bice sacuvano u folderu
												# gde se nalazi i ovaj .py file