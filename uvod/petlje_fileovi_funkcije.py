"""
Skripta broj 2.

Rad sa petljama (for, while, if), ucitavanje i upisivanje u file kao i 
definisanje funkcija.

23. februar 2018.
"""

l = [1, 5.3, 'Python3', False, 1.232e-2] # lista

"""
for petlja - izvrsavamo neki niz operacija zadati broj puta
"""
for element in l: 					# u prevodu: za svaki 'element' iz liste 'l' radi nesto
	print (element) 				# obratiti paznju da je red uvucen tacno 4 blanko mesta! ili jedan tab

for ii in range(len(l)):			# mozemo ici i po indeksima.
	print (l[ii])					# napomena: indeksira se od 0 i promenljiva 'ii' ce imati
									# 			vrednosti od 0 do len(l)-1

"""
while petlja - izvrsavamo neki niz operacija dok je zadovoljen uslov

U okviru while i if petlje se koriste sledeci logicki operatori (u formatu
element1 operator element2)
	
	==  - jednakost medju elementima
	!=  - razlicitost elemenata
	>   - vece
	< 	- manje
	and - logicko i
	or  - logico ili
	not - logicka negacija
"""
ii = 0
while ii < len(l):
	print (l[ii])
	ii += 1 						# brojac kroz listu, na pocetku moramo zadati da je jednak 0;
									# skraceni zapis za: ii = ii + 1 je ii += 1

"""
if petlja - uslovna petlja: ako je nesto tacno, izvrsava se odrejeni deo kod,
			u suprotnom, ide se u else granu (opciono) i izvrsava se drugi deo kod
"""
print ()
l = [1,2,3,4,5,6,7,8,9]
for broj in l:						# za svaki broj iz liste proveravamo da li je deljiv sa brojem 3,
	if broj%3 == 0:					# ako jeste, ispisuje se taj broj, u suprotnom se ispisuje 'nije deljiv'
		print ('broj ', broj, ' je deljiv brojem 3')
	else:
		print ('broj ', broj, ' nije deljiv sa brojem 3')
		# vidite da je sa svakim uslovom kod uvucen za 4 blanko mesta ili jedan tab!

"""
Ucitavanje i ispisivanje iz file-a.

Tekst koji ucitavamo moze biti proizvoljnog tipa posto na kraju to biva ucitano
kao string. Kasnije to mozemo pretvoriti u broj ako su u pitanju podaci iz nekog
eksperimenta ili baze podataka.
"""
f = open('test_podaci', 'r')		# opsti nacin otvaranja file-a za citanje sadrzaja

for line in f.readlines():			# f.readlines() - ucitali smo sve linije u jednu listu i prolazimo kroz njih
	print (line.rstrip('\n'))		# printamo svaku liniju (tipa string) iz file-a koji smo upravo ucitali
									# funkcija '.rstrip' skida odgovarajuci karakter sa kraja datog stringa;
									# karakter '\n' predstavlja oznaku za novi red
f.close()							# zatvaramo file kada nam vise nije potreban

f = open('izlaz_podaci', 'w')		# mozemo i ispisivati stvari u file
f.write('Ovo je prva linija teksta \n')
f.write('a ovo druga u file-u!')
f.write('\n a to mozemo i' + '\t' + 'ovako da upusujemo :)') # '\t' - oznaka za jedan tab razmak u tekstu
f.close()

"""
Funkcije - pre nego sto se definise funkcija stoji kljucna rec 'def'. Promenljive unutar funkcije
i njihove vrednosti nisu vidljive, ne moze im se pristupiti, van funkcija. Medjutim, promenljivima
definisanim van funkcija se moze pristupiti unutar funkcija. Zbog toga voditi racuna o nazivima
promenljivih u funkcijama.

"""
def sabiranje(a, b):
	c = a + b 						# funkcija koja se zove 'sabiranje', ima argumente 'a' i 'b' i vraca
	return c 						# zbir argumenata funkcije

print (sabiranje(2,3))

def stepenovanje(a, stepen = 2):	# funkcija moze da ima i argumente koji su default kao sto je stepen
	broj = a**stepen
	return broj

print (stepenovanje(3))				# racunamo 3**2
print (stepenovanje(3, stepen = 5))	# racunamo 3**5 - promenili smo default argument na 5

def exmpl(broj):
	a = broj**0.5
	b = broj%2
	return a,b 						# funkcija moze i da vraca vise od jednog argumenta

out = exmpl(13)						# sada je 'out' promenljiva tipa tuple
print (out)

fun = lambda x: x + 10				# ako imamo proste funkcije mozemo ih definisati u jednoj liniji
print (fun(10))						# uz pomoc kljucne reci 'lambda' gde je 'x' argument funkcije