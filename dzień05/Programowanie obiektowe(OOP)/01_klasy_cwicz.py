class Produkt:
    def __init__(self, cena, nazwa, id):        #konstruktor (metoda konstruktora) (magiczna bo ma__)

        self.cena = cena                        #atrybuty
        self.nazwa = nazwa
        self.id = id

    def wypisz_info(self):                      #metody(funkcje)
        print(f"Produkt: {self.nazwa} ID: {self.id} Cena: {self.cena}")


mydlo = Produkt("10pln", "Mydło", "12")         #wywołanie konstruktora / stworzenie obiektu
szampon = Produkt("20pln", "Szampon", "22")


mydlo.wypisz_info()                             #wywołanie metody
szampon.wypisz_info()

