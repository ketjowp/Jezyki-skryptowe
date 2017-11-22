x=int(input("Podaj rok:\n"))

if (x%4==0 and x%100!=0) or (x%100==0 and x%400==0):
    print("Rok przestępny")
else:
    print(("Rok nieprzestępny"))
