c=input("Podaj cyfrę: ")
s={'1':'jeden','2':'dwa','3':'trzy','4':'cztery','5':'pięć','6':'sześć','7':'siedem','8':'osiem','9':'dziewięć','0':'zero'}
if c.isdigit and len(c)==1:
    w=s.get(c)
    print(w)
else :
    print("Miałeś podać cyfrę")
