import pickle
imiona=list()
zenskie=list()
meskie=list()
try:
    with open("zenskie.txt","rb") as f:
        zenskie=pickle.load(f) #czy txt?
    with open("meskie.txt","rb") as f:
        meskie=pickle.load(f)
    imiona=meskie+zenskie
    meskie.clear()
    zenskie.clear()
except FileNotFoundError:
    pass
finally:
    while True: 
        wpis=input("Podaj imię: ")
        if wpis.lower()!="koniec":
            if wpis.isalpha():
                if imiona.count(wpis.title())==0:
                    imiona+=[wpis.title()]
                else:
                    print("Imię znajduje sie już na liście")
            else:
                print("Miałeś podać imię")
        else:
            for i in range(len(imiona)):
                if imiona[i][-1]=="a" and imiona[i]!="Kosma" and imiona[i]!="Barnaba" and imiona[i]!="Bonawentura" and imiona[i]!="Jarema" and imiona[i]!="Kuba":
                    zenskie.append(imiona[i])
                else:
                    meskie.append(imiona[i])
            print("Oto lista imion męskich:")
            meskie.sort()
            for i in range(len(meskie)):
                print(meskie[i])
            print("Oto lista imion żeńskich:")
            zenskie.sort()
            for i in range(len(zenskie)):
                print(zenskie[i])
            with open("zenskie.txt","wb") as f:
                pickle.dump(zenskie,f)
            with open("meskie.txt","wb") as f:
                pickle.dump(meskie,f)
            break
