class Przedmiot:
    def __init__(self, nazwa, bonus):
        self.nazwa = nazwa
        self.bonus = bonus

    def __str__(self):
        return f"{self.nazwa=},{self.bonus=}"


class Postac:
    def __init__(self, imie, max_zdrowie, atak):
        self.imie = imie
        self.max_zdrowie = max_zdrowie
        self.zdrowie = max_zdrowie
        self.atak = atak
        self.ekwipunek = []

    def daj_przedmiot(self, p: Przedmiot): #p: Przedmiot to jest type hint (nie zmienia działania programu), że p powinno być typem przedmiot. Np. pycharm to wtedy podkreśli
        #if type(p) != Przedmiot:  #można tak zrobić sprawdzenie że p jest klasą Przedmiot
        if not isinstance(p, Przedmiot):   #ale lepiej tak
            print("Błąd!")
            return
        self.ekwipunek.append(p)

    def wypisz_ekwipunek(self):
        print("Ekwipunek")
        for p in self.ekwipunek:
            print(p)

    def wypisz_info(self):
        print(f"{self.imie}, zdrowie: {self.zdrowie}/{self.max_zdrowie}, atak: {self.daj_atak()}")

    def czy_zyje(self):
        return self.zdrowie > 0

    def otrzymaj_obrazenia(self,dmg):
        self.zdrowie -= dmg
        if self.zdrowie < 0:
            self.zdrowie = 0

    def wylecz(self, x):
        if self.czy_zyje():
            self.zdrowie += x
        #    if self.zdrowie > self.max_zdrowie:
        #        self.zdrowie = self.max_zdrowie
        #alternatywnie: (krócej)

            self.zdrowie = min(self.zdrowie + x, self.max_zdrowie)
        else:
            print(f"{self.imie} już nie żyje")


    def daj_atak(self):
        return self.atak



#można też repr-em:
#    def __repr__(self):
#        return f"Przedmiot({self.nazwa!r},{self.bonus=})"



rufus = Postac("Rufus",100,4)
kij = Przedmiot("kij", 4)   ###
rufus.daj_przedmiot(kij)        ### tu miałem problem po prostu tworzę obiekt klasy z klasą w argumencie!
rufus.daj_przedmiot(123)    #tu mam sprawdzenie żeby nie działało
rufus.wypisz_ekwipunek()
