from math import sin, cos, radians

class Zolw:
    def __init__(self,x,y,kierunek):
        self.x = x
        self.y = y
        self.kierunek = kierunek #kąt między kierunkiem a osią x

    def wypisz(self):
        print(self.x, self.y, self.kierunek)

    def lewo(self, n):
        self.kierunek += n

    def prawo(self, n):
        self.kierunek -= n

    def naprzod(self, n):
        self.x += n * cos(radians(self.kierunek)) #trzeba zamienic stopnie na radiany bo w math sin i cos dzialają na radianach
        self.y += n * sin(radians(self.kierunek))

z = Zolw(0,0,0)
z.wypisz()
z.lewo(45)
z.naprzod(1)
z.wypisz()