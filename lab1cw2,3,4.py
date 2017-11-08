tekst ="""Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.

Panno Święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
Nowogródzki ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem
(Gdy od płaczącej matki pod Twoję opiekę
Ofiarowany, martwą podniosłem powiekę
I zaraz mogłem pieszo do Twych świątyń progu
Iść za wrócone życie podziękować Bogu),
Tak nas powrócisz cudem na Ojczyzny łono.
Tymczasem przenoś moję duszę utęsknioną
Do tych pagórków leśnych, do tych łąk zielonych,
Szeroko nad błękitnym Niemnem rozciągnionych;
Do tych pól malowanych zbożem rozmaitem,
Wyzłacanych pszenicą, posrebrzanych żytem;
Gdzie bursztynowy świerzop, gryka jak śnieg biała,
Gdzie panieńskim rumieńcem dzięcielina pała,
A wszystko przepasane, jakby wstęgą, miedzą
Zieloną, na niej z rzadka ciche grusze siedzą."""
print(tekst)
l=len(tekst)
m = tekst.lower() 
a = m.count('a')
ą = m.count('ą')
e = m.count('e')
ę = m.count('ę')
i = m.count('i')
o = m.count('o')
u = m.count('u')
y = m.count('y')
s = a+ą+e+ę+i+o+u+y
kropki = tekst.count('.')
spacje = tekst.count(' ')
przecinki = tekst.count(',')
print('Tekst zawiera ',l,' znaków, w tym: ',s,' samogłosek, ',kropki, ' kropek, ',przecinki,' przecinków i ',spacje,' spacji.\n')
print('Co drugi znak:\n'+tekst[::2]+'\n\nCo trzeci znak:\n'+tekst[::3]+'\n\nCo siódmy znak:\n'+tekst[::7])
lista=tekst.splitlines()
print('Pierwszy wers:\n'+lista[0])
print(lista[0].upper())
print(lista[0].replace('Litwo!','Polsko!'))
