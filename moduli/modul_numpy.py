"""
Skripta broj 3.

Rad sa modulima - numpy

Mouli sadrze skup razlicitih funkcija koje se pozivaju u formatu:
naziv_modula.ime_funkcije(objekat_na_koji_primenjujemo_funckiju)

Numpy modul sadrzi operacije nad numericim nizovima (type je ndarray) koji
mogu biti proizvoljnog broja dimenzija.

23. februar 2018.
"""

import numpy as np
# ucitavamo modul 'numpy' i skraceno ga zovemo 'np'
from numpy import loadtxt

# u ovom formatu ucitavamo samo odredjene funkcije
# koje se nalaze unutar modula kao sto je npr. 'loadtxt'

# =================================== #
a = [1, 2, 3, 4, 5, 6]
a = np.array(a)
# promenili smo tip liste u numpy niz
print(a)
print(a * 2)
# bitna razlika nmerickih nizova od liste je sto ako ih pomnozimo
# nekim brojem, onda taj broj mnozi svaki element numerickog
# niza dok kod obicnih python lista, red se kopira x puta

# =================================== #

a = np.linspace(1, 12, num=20)
# niz od 20 ravnomerno rasporedjenih vrednosti od 1 do 12
a = np.logspace(0, 1.1, num=20)
# niz od 20 logaritamski ravnomerno rasporedjenih tacaka od 10^0 do 10^1.1
a = np.arange(1, 12, 0.5)
# niz od 1 do 12 sa ravnomerno rasporedjenim vrednostima sa
# korakom od 0.5

# =================================== #

np.sum(a)
# zbir svih elemenata niza 'a' ili a.sum()
np.prod(a)
# proizvod svih elemenata niza 'a' ili a.prod()
a = np.append(a, 2)
# dodavanje novog elementa, broja 2, na kraj niza

# =================================== #

a = np.random.random(5)
# generisanje niza od 5 random float brojeva u intervalu (0,1)
b = np.random.random(5)
print(a + b)
# nad nizovima mozemo primeniti iste operacije kao i nad
print(a - b)
# obicnim brojevima, samo ta dva niza moraju biti istih dimenzija!
print(a * b)
# (da imaju isti broj elemenata)
print(a / b)

# =================================== #

print(max(a), min(a))
# maximalni i minimalni element niza a
print(np.argmax(a), np.argmin(a))
# indeksi maksimalnog i minimalnog elementa niza a

# =================================== #

c = np.vstack((a, b))
# vertikalno dodavanje jednog niza na drugi - prelepili smo jedan
print(c)
# preko drugog - dobili smo matricu sa 2 reda i len(a) kolona
print(c.shape)
# dimenzija promenljive 'c' - prvi broj je broj redova, drugi je
# broj kolona

c = np.hstack((a, b))
# horizontalno smo dodali jedan niz drugom - u nastavku prvog
print(c)
# smo dodali elemente drugog - novi niz duple duzine
print(c.shape)

# =================================== #

niz = np.zeros(10)
# niz od 10 elemenata gde su svi nula
matrica = np.zeros((2, 3, 4))
# matrica dimenzija 2,3,4 koja ima sve nule
matrica = np.ones((50, 10, 20, 2, 2))
# matrica sa svim nulama

# =================================== #

a = np.random.randint(9, size=(3, 3))
# definisali smo random niz celih brojeva i promenili ga u
b = np.random.randint(9, size=(3, 3))
# matricu dimenzija 3x3

print(a[0, :])
# printanje svih elemenata iz prvog reda, isto bi isli i samo a[0]
print(a[:, 0])
# printanje svih elemenata iz prve kolone
print(np.sum(a))
# suma svih elemenata u matrici
print(np.sum(a, axis=0))
# suma svih elemenata u matrici - sumira elemente po svim redovima

c = a * b
# samo ce pomnoziti odgovarajuce elemente u matricama - nije matricno mnozenje!
print(c)
# i kod matrica vaze sve osnovne operacije kao i kod nizova sto
# sto vaze (+ - * / //, ali su elemen-po-element)

# =================================== #

c = np.dot(a, b)
# proizvod dveju matrica
print(c)
print(np.linalg.inv(a))
# inverzna matrica
print(np.transpose(a))
# transponovana matrica; skraceno samo c.T
print(np.linalg.det(a))
# determinanta matrice
print(np.trace(a))
# trag matrice
print(np.diagonal(a))
# elementi sa dijagonale matrice

# =================================== #

c = np.sort(c, axis=-1)
# sortiramo vrednosti u matricu duz poslednje dimenzije (to je po defaultu)
c = np.sort(c, axis=0)
# sortiramo prema prvoj dimenziji - duz kolone je sortirano (svaki prvi
# element u datom redu je najmanji) to znaci prema prvoj dimenziji
c = np.sort(c, axis=None)
# sortiramo elemente u matrici i ispeglamo to u jedan niz

# =================================== #

data = np.loadtxt('test_podaci')
# ucitavanje numerickih podataka iz datog file-a
# file moze imati bilo koju ekstenziju (.txt, .dat, .csv i slicno), samo
# je bitno da svaka kolona ima isti broj vrednosti i da su sve brojevi
# (bilo int bilo float)
t1, t2, t3 = np.loadtxt('test_podaci', unpack=True)
# mozemo da ucitamo i po kolonama odmah raspakujemo
# za detalje o funkciji 'loadtxt' videti na:
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
# mozemo i da cuvamo podatke uz pomoc 'savetxt', probajte sami da se poigrate!

# =================================== #

a = np.sin(np.pi)
# u numpy modulu su i razne matematicke funkcije koje na niz deluju tako sto
# pojedinacno deluju na svaki element niza.
# Trigonometrijske funkcije za argument uzimaju radijane!
# np.cos, np.tan, np.arctan, np.arcsin, np.arccos. np.pi je broj pi
a = np.exp(2)
# exponencijalna funkcija
a = np.log(10)
# logaritamska funkcija; po defaultu je osnova Ojlerov broj; np.log10 ima za
# osnovu broj 10, np.log2 sa osnovom 2
