"""

Transformacija koordinata nebeskog objekta iz mesnog ekvatorskog u
horizontski koordinatni sistem.

azurirano: 25. mart 2018.

"""

import numpy as np

# geografska sirina [deg]
phi = 45
# deklinacija [deg]
dek = 25
# casovni ugao [h]
cas = 1.24

if dek==phi and cas==0:
	print("Date koordinate predstavljaju zenit!")
	print("Azimut je neodredjen dok visina iznosi 90 \n")
else:
	if dek==-phi and cas==12:
		print("Date koordinate predstavljaju nadir")
		print("Azimut je neodredjen dok visina iznosi -90 \n")
	else:
		# pretvaramo koordinate u radijane
		dek = dek * np.pi/180
		cas = cas * 15*np.pi/180
		phi = phi * np.pi/180

		prva = np.sin(dek)*np.sin(phi) + np.cos(dek)*np.cos(phi)*np.cos(cas)
		druga = np.cos(dek)*np.sin(cas)
		treca = -np.cos(phi)*np.sin(dek) + np.sin(phi)*np.cos(dek)*np.cos(cas)

		aux = (druga**2 + treca**2)**0.5

		# arctan2 funkcija umesto nas proverava u kom kvadrantu je objekat i
		# vraca odgovarajuci ugao
		azm = np.arctan2(druga, treca)
		vis = np.arctan2(prva, aux)

		# vracamo nazad u stepene
		azm = azm * 180/np.pi
		vis = vis * 180/np.pi

		print("Azimut: ", azm, " deg")
		print("Visina: ", vis, " deg")
