import math

print("ax^2+bx+c=0")
a=int(input("podaj parametr a:\n"))
b=int(input("podaj parametr b:\n"))
c=int(input("podaj parametr c:\n"))
d=(b**2)-4*a*c


if a!=0:
    if d>0:
        x1=(-b-math.sqrt(d))/2*a
        x2=(-b+math.sqrt(d))/2*a
        print("Pierwszy pierwiastek: ",x1,"Drugi pierwiastek: ",x2)
    elif d==0:
        x0=(-b/2*a)
        print("Istnieje jeden pierwiastek x0=",x0)
    else:
        print("brak pierwiastków rzeczywistych")
else:
    x0=-c/b
    print("Rozwiązanie równania liniowego to x=",x0)
