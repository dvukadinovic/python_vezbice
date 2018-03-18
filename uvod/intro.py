"""
Skripta broj 1.

Osnovni primeri rada u Pythonu i operacije nad promenljivima.

23. februar 2018.
"""

# in-line komentar
"""
Blok
komentar
"""
"""
print (nesto) - na standardni izlaz ispisujemo sadrzaj unutar
obicnih zagrada. Moze biti broj / slovo / tekst ili sta god.
"""

print(2 + 2)
print(2 + 3.5)
print(3.41 - 2)
print(24 / 13)
print(24 // 13)
print(2 * 2.232)
print(2**5)
print(16**(0.5))
print(124 % 3)
"""
type (nesto) - funkcija type nam vraca kog je tipa promenljiva koja
se nalazi unuatr obicnih zagrada.

Tipovi koji se srecu su:
- int : celobrojni tip
- float : decimalni tip
- str : string ili obican tekst
- bool : logicki tip (True ili False)
- NoneType : bez tipa
- dictionary
- tuple 
- class
- ....
"""

a = 5
print(type(a))

a = 2.71
print(type(a))

a = "ucimo Python3"
b = 'koji je interesantan'
print(type(a))
print(type(b))

a = True
print(type(a))
"""
Prethodni primeri sadrze samo jednu vrednost. Medjutim, vise promenljivih
mozemo i da grupisemo u jednu. Takvi tipovi se nazivaju: liste, tuple-ovi, 
recnici i nizovi (njih cemo malo kasnije podrobnije sresti kada budem 
radili sa numpy modulom).
"""

l = [1, 5.3, 'Python3']  # lista
print(l)
"""
Mozete pristupiti i samo nekom elemntu liste / niza ili vise njih.
Python broj od 0, sto znaci da je prvi element sa indeksom 0. A mozete
i brojati unazad, tako da je -1 element poslednji, -2 pretposlednji itd.
"""
print(l[0])
print(l[-1])

l[0] = 23  # menjamo vrednost prvog elementa u listi
print(l)
print(l * 2)  # duplirali smo listu - napravili njenu kopiju
print((l * 2)[1:5:2])  # od 1. do 5. elementa, ali svaki drugi element
print((l * 2)[::3])  # svaki treci element iz cele liste

l.append(
    False
)  # dodajemo novu promenljivu na kraj liste - zato se koristi funkcija append (nesto)
print(l)
print(len(l))  # len (nesto) - vraca duzinu promenljive koja se
# nalazi u obicnim zagradama

print(l[1:3])  # printamo samo elemente sa indeksom 1 sve do
# elementa sa indeksom 3 (ne ukljucujuci taj indeks)
# ukoliko ne bi stajao broj 3, onda bi se uzeli elementi
# sve do poslednjeg. Poigrajte se sa tim.

t = (1, 5.3, 'Python3')  # tuple; slicno kao i lista, samo sto je sa obicnim
# zagradama; razlika u odnosu na liste je samo sto
# ne mozemo da menjamo vrednosti unutar tuple-a
# ostale operacije koje vaze za liste, vaze i za
# tuple-ove

# int()     - pretvaramo u ceo broj
# float()   - pretvaramo u decimalni broj
# str()     - pretvaramo u string
a = '5'
print(type(a))
b = int(a)
print(type(b), b)
c = float(a)
print(type(c), c)

a = 5.21
b = int(a)
print(type(b), b)
c = str(a)
print(type(c))
