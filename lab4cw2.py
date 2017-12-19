import math

class Punkt(object):
    def __init__(self,x=0,y=0):
        if (type(x)==int or type(x)==float) and (type(y)==int or type(y)==float):
            self.x=x
            self.y=y
        else:
            print("Współrzędne punktu muszą być liczbami")
    def odleglosc(self):
        return math.sqrt(self.x**2+self.y**2)
    def dystans(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    def __repr__(self):
        return ("Punkt(%g,%g)"%(self.x,self.y))
    def __str__(self):
        return ("(%g,%g)"%(self.x,self.y))

class Kolo(Punkt):
    def __init__(self,x=0,y=0,r=1):
        Punkt.__init__(self)
        self.r=r
