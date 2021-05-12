# __  'magic methods, albo dunder methods (double underscore)

class Osoba:        #tworzymy wartość typu Osoba (nie, int, nie dict..itd)
    #magiczna metoda __init__() jest wywołana w momencie tworzenia obiektu
    #self jest obiektem który własnie tworzymy

    def __init__(self, imie,nazw):
        print("Tworzę osobę")
        self.imie = imie
        self.nazwisko = nazw


    def powiedzCos(self):           #metoda/funkcja klasy Osoba
        print("Jestem Osobą")

    def przedstawSie(self):     #pierwszy argument (self) jest obiektem na ktorym została wywołana metoda
        print(f"nazywam się{self.imie} {self.nazwisko}")

jan = Osoba("Jan", "Nowak")
ania = Osoba("Ania", "Kowalska")

jan.przedstawSie()
ania.przedstawSie()



## wariant z konstruktorem z argsami

class Osoba:        #tworzymy wartość typu Osoba (nie, int, nie dict..itd)
    #magiczna metoda __init__() jest wywołana w momencie tworzenia obiektu
    #self jest obiektem który własnie tworzymy

    def __init__(self, *args):
        print("Tworzę osobę")
        self.imie = args[0]
        self.nazwisko = args[1]

#    def inicjuj(self, imie):
#        self.imie = imie  #ustawiamy atrybut self.imie na imie przekazane jako argument

    def powiedzCos(self):           #metoda/funkcja klasy Osoba
        print("Jestem Osobą")

    def przedstawSie(self):     #pierwszy argument (self) jest obiektem na ktorym została wywołana metoda
        print(f"nazywam się{self.imie} {self.nazwisko}")

jan = Osoba("Jan", "Nowak")
ania = Osoba("Ania", "Kowalska")

jan.przedstawSie()
ania.przedstawSie()
