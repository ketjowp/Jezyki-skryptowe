def funkcja(a):
    if a<0:
        print("-1000")
    elif a==0:
        print("ZEROOOO!!!!")
    elif a>0 and a<10:
        print(a)
    elif a>=10 and a<=100:
        print("dużo")
    elif a>100:
        print("bardzo dużo")

while True:
    x=input("Podaj liczbę:\n")
    
    if x.isdigit() or (x[0]=='-' and x[1:].isdigit()):
        liczba=int(x)
        funkcja(liczba)
    else:
        print("To nie jest liczba")
        break
