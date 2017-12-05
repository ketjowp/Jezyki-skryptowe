imiona=list()
dlugosc=10
for i in range(dlugosc):
    wpis=input("Podaj imię: ")
    if wpis.isalpha():
        if imiona.count(wpis)==0:
            imiona+=[wpis.title()]
        else:
            print("Imię znajduje sie już na liście.")
    else:
        print("Miałeś podać imię: ")
print("Oto lista imion:")
print(imiona)

