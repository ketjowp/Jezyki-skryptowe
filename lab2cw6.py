a=0
b=1
n=int(input("Podaj liczbę wyrazów ciągu Fibbonacciego n:\n"))
for i in range(0,n):
    print(b)
    b=a+b
    a=b-a
