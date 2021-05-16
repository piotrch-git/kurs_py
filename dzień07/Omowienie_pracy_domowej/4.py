
class Robot:
    def __init__(self,x,y,kierunek):
        self.x=x
        self.y=y
        self.kierunek = kierunek


    def wypisz(self):
        kierunki = ('N','E','S','W')
        print(self.x,self.y,kierunki[self.kierunek])


    def lewo(self):
        self.kierunek = (self.kierunek -1) % 4  #modulo z liczb ujemnych w niektórych językach (np c) nie działa jak powinno. Tutaj jest OK.


    def prawo(self):
        self.kierunek = (self.kierunek + 1) % 4


    def naprzod(self):
    #    if self.zwrot % 4 == 0:
    #        self.y += 1
    #    elif self.zwrot % 4 == 1:
    #        self.x += 1
    #    elif self.zwrot % 4 == 2:
    #        self.y -= 1
    #    elif self.zwrot % 4 == 3:
    #        self.x -= 1

        x, y = ((0,1),(1,0), (0,-1), (-1,0))[self.kierunek]
        self.x += x
        self.y += y


    def wykonaj(self,instrukcje: str):  #tutaj znowu king że instrukcje mają być stringiem
       # for i in instrukcje:
       #     if i == "P":
       #         self.prawo()
       #     elif i == "L":
       #         self.lewo()
       #     elif i == "N":
       #         self.naprzod()
        metody = {'N':self.naprzod, 'L':self.lewo, 'P':self.prawo}  # funkcje bez nawiasów bo nie chcemy wywoływać tych metod, tylko je przekazać.
        for i in instrukcje:
            metody[i]()  #tutaj jest pusty nawias bo to tutaj wywołujemy te metody



r = Robot(0,0,0)
r.wypisz()
r.naprzod()