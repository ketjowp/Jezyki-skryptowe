x=input('Podaj cyfrę: ')
y=input('Podaj cyfrę: ')
z=input('Podaj cyfrę: ')
if(x.isdigit() and len(x)==1 and y.isdigit() and len(y)==1 and z.isdigit() and len(z)==1):
    liczba=x+y+z
    print(int(liczba),int(liczba)**2)
else:
    print('Miałeś podać cyfry!')
