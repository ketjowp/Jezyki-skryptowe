x=input("Podaj liczbę:\n")
liczba=int(x)

if x.isdigit() or (x[0]=='-' and x[1:].isdigit()):
    if liczba<0:
        print("-1000")
    elif liczba==0:
        print("ZEROOOO!!!!")
    elif liczba>0 and liczba<10:
        print(liczba)
    elif liczba>=10 and liczba<=100:
        print("dużo")
    elif liczba>100:
        print("bardzo dużo")
else:
    print("To nie liczba")
