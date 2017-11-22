import cmath

print("ax^2+bx+c=0")
a=int(input("podaj parametr a:\n"))
b=int(input("podaj parametr b:\n"))
c=int(input("podaj parametr c:\n"))
d=(b**2)-4*a*c

x1=(-b-cmath.sqrt(d))/2*a
x2=(-b+cmath.sqrt(d))/2*a

print("Pierwiastki tego równania to x1=",x1," x2=",x2)
