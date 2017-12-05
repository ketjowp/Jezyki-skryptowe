imiona=list()
while True: 
    wpis=input("Podaj imię: ")
    if wpis.lower()!="koniec":
        if wpis.isalpha():
            if imiona.count(wpis.title())==0:
                imiona+=[wpis.title()]
            else:
                print("Imię znajduje sie już na liście")
        else:
            print("Miałeś podać imię: ")
    else:
        print("Oto lista imion:")
        imiona.sort()
        with open("imiona.txt","w") as f:
            for i in range(len(imiona)):
                f.write(imiona[i]+"\n")
                print(imiona[i])
        break
