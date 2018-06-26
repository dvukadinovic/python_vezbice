"""

!Napomena. Ovaj primer je dodatak na sve one koje ste vec sretali prilikom
!rada u IDL-u. Topla je preporuka da prodjete kroz ovaj primer, ali pre toga
!prodjite rad sa fajlovima, modulima, fits snimcima, raznim plotovanjem i
!slicno.

Numericko resavanje diferencijalne jednacine kretanja tela u gravitacionom
polju Zemlje - kosi hitac, za koji znamo tacno analiticko resenje. Ideja je da
se napise Ojelrov integrator za ovaj primer, a na studentu je da po volji
prosiri kod i doda npr. silu otpora sredine i posmatra kako ce kretanje kroz
razlicitu sredinu, ili sa drugacijim koeficijentom otpora, uticati na
trajektoriju cestice. Ovaj problem kasnije moze da se prosiri i na
suborbitalni let rakete ili letelice.

Sistem diferencijalnih jednacina koje cemo resavati su:

	dx/dt = C1	i	dy/dt = - g*t + C2

Ostavlja se studentu da pokaze da ove jednacine slede iz II Njutnovog zakona
za kretanje tela. Dati sistem je sveden na diferencijlne jednacine prvog reda.
Posto su jednacine razdvojene, mozemo ih posebno resavati. Obicno, to ne mora
biti slucaj.

O Ojlerovom integratoru mozete procitati na:
http://www.maths.lth.se/na/courses/FMN050/media/material/part14.pdf. Studentu
se ostavlja da sam implementira i Runge-Kutta metod bilo drugog ili cetvrtog
reda koje su stabilnije, preciznije i cesce koriscenje metode (vise o tome na:
http://tnt.phys.uniroma1.it/twiki/pub/TNTgroup/AngeloVulpiani/runge.pdf).

azurirano: 26. jun 2018.

"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81 # [m/s2]

# iz jednacina se vidi da su C1 i C2 trenutne brzine cestice; integraciju
# krecemo od t=0, tako da ce nam C1 i C2 onda predstavljati pocetene brzine
# duz x i y ose, respektivno. Posto je u pitanju sistem od 2 jednacine 2.
# reda, to znaci da su nam potrebna 4 pocetna uslova: 2 za poziciju i 2 za
# brzinu (ili ukupnu brzinu i ugao izbacaja).

# zadajemo ukupnu pocetnu brzinu i ugao izbacaja cestice
v = 50 # [m/s]
tht_list = [30, 45, 60] # [deg]

# sada za svako theta iz liste racunamo trajektoriju i prikazujemo ih sve na
# jendom grafiku kako bismo mogli da ih uporedimo; kod koji se nalazi u okviru
# for petlje mozemo da izvucemo napolje i uradimo samo ze jedno tht koje
# iniciramo (preporucujem da to probate pre nego sto uopstite na vise uglova)
for tht in tht_list:
	# racunamo pocetne brzine cestice duz svake komponente kretanja
	C1 = v * np.cos(np.deg2rad(tht))
	C2 = v * np.sin(np.deg2rad(tht))

	# definisemo pocetni trenutak i vremenski korak integracije
	t = 0
	dt = 0.01 # [s]

	# definisemo pocetne vrednosti pozicij cestice; stavljamo ih u lisu koju cemo
	# prosirivati kako budemo integralili trajektoriju
	x = [0]
	y = [0]

	# integralimo sve dok nam cestica ne padne na pod
	while y[-1]>=0:
		# racunamo narednu poziciju cestice na osnovu prethodne
		# Ojlerov korak
		aux_x = x[-1] + C1*dt
		aux_y = y[-1] + (-g*t + C2) * dt
		# dodajemo u listu novu poziciju
		x.append(aux_x)
		y.append(aux_y)
		t += dt

	plt.plot(x, y, label=tht)

plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend(loc='best', frameon='False')
plt.show()