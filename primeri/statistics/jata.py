"""

Sa Vizier baze podataka naci katalog 'Optically visible open clusters and
Candidates' (Dias 2002-2014) i skinuti podatke o poziciji. Potrebno je
predstaviti raspodelu jata u heliocentricnim pravouglim koordinatama (3D
plot). Udaljenost jata je podjednaka, tako da ce posmatrana rapsodela
ocrtavati raspodelu na nebeskoj sferi.

Posle toga, napraviti raspodelu jata u galaktocentricnom Dekartovom
koordinatnom sistemu prema poznatim rastojanjima jata od Sunca. Rastojanje
Sunca od galaktickog centra je 8.3 kpc. Ujedno razmotriti raspodelu jata po
udaljenosti od galakticke ravni.

azurirano: 25. jun 2018.

"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import astropy.units as u
import astropy.coordinates as coord

alpha, delta, dist = np.loadtxt('jata', unpack=True)
dist = dist * 1e-3 # [kpc]

# prebacujemo uglove u radijane
alpha = np.deg2rad(alpha)
delta = np.deg2rad(delta)

# heliocentricne koordinate
x = np.cos(delta)*np.cos(alpha)
y = np.cos(delta)*np.sin(alpha)
z = np.sin(delta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xs=x, ys=y, zs=z, s=4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

# transformacija koordinata - koristimo astropy modul
helio = coord.ICRS(ra=alpha*u.rad, 
				   dec=delta*u.rad, 
				   distance=dist * u.kpc)
galc = helio.transform_to(coord.Galactocentric)
X,Y,Z = galc.x.data, galc.y.data, galc.z.data

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# oznacavamo galakticki centar
ax.scatter(0,0,0, marker = '*', color = 'magenta', s = 25)

ax.scatter(xs=X, ys=Y, zs=Z, s=3)
ax.set_xlabel('X [kpc]')
ax.set_ylabel('Y [kpc]')
ax.set_zlabel('Z [kpc]')
plt.show()

plt.hist(Z, bins=20, histtype='step')
plt.xlabel(r'$Z [kpc]$')
plt.ylabel(r'$N$')
plt.show()