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
        super().__init__(x,y)
        self.r=r
    def obwod(self):
        return math.pi*2*self.r
    def pole(self):
        return math.pi*self.r**2
    def przesun(self,list):
        self.x+=list[0]
        self.y+=list[1]
    def __repr__(self):
        return ("Kolo o promieniu %g i środku (%g,%g)"%(self.r,self.x,self.y))
    def __str__(self):
        return ("Promien %g, środek (%g,%g)"%(self.r,self.x,self.y))

k1=Kolo(2,3,4)
k2=Kolo(4,3,2)
