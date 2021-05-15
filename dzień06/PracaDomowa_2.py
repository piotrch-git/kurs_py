# 0. Do klasy Postac (z zajęć) dodaj atrybut 'atak' (będący liczbą) ustawiany w konstruktorze oraz metodę daj_atak(), która zwróci wartość ataku Postaci.
#
# 1. Stwórz klasę Przedmiot, który będzie posiadał nazwę i jakiś bonus liczbowy (np. Przedmiot("Kij", 4) => Przedmiot o nazwie "Kij" i bonusie 4) oraz będzie posiadał sensowną reprezentację napisową (metoda __str__()).
#
# 2. Rozszerz klasę Postać (zad 0.) o ekwipunek - dodaj metody:
# 	- daj_przedmiot(p) - dodaje Przedmiot(zad 1.) do ekwipunku,
# 	- wypisz_ekwipunek - wypisuje wszystkie Przedmioty posiadane przez daną Postać.
#
# 3. W klasie Postać (zad 0.) zmodyfikuj metodę daj_atak(), żeby zwracała wartość ataku Postaci powiększoną o sumę bonusów z posiadanych w ekwipunku(zad 2.) Przedmiotów(zad 1.).
#

class Postac:
    def __init__(self, imie, max_zdrowie):
        self.imie = imie
        self.max_zdrowie = max_zdrowie
        self.zdrowie = max_zdrowie
        self.atak = 10
        self.ekwipunek = []

    def daj_atak(self):
        if self.czy_zyje():
            print(f"{self.atak}")
        else:
            print("Martwy nie może atakować")

    def wypisz_info(self):
        print(f"{self.imie}, zdrowie: {self.zdrowie}/{self.max_zdrowie}")

    def czy_zyje(self):
        return self.zdrowie > 0

    def otrzymaj_obrazenia(self, dmg):
        self.zdrowie -= dmg
        if self.zdrowie < 0:
            self.zdrowie = 0

    def wylecz(self, x):
        if self.czy_zyje():
            self.zdrowie += x
            #    if self.zdrowie > self.max_zdrowie:
            #        self.zdrowie = self.max_zdrowie
            # alternatywnie: (krócej)

            self.zdrowie = min(self.zdrowie + x, self.max_zdrowie)
        else:
            print(f"{self.imie} już nie żyje")

    def daj_przedmiot(self,p):
   #     if isinstance(p, Przedmiot):
        self.ekwipunek.append(p)
    #    else:
    #        print("daj mi Przedmiot")

    def wypisz_ekwipunek(self):
        print(f"{self.imie} posiada: {self.ekwipunek}")

class Przedmiot:
    def __init__(self,p,bonus):
        self.p=p
        self.bonus=bonus
    def __str__(self):
        return f"{self.p=},{self.bonus=}"

#O to jakas zmiana
lyzka = Przedmiot("lyzka",10)
print(lyzka)
rufus = Postac("Zenek", 200)
rufus.wypisz_ekwipunek()
rufus.daj_przedmiot(Przedmiot("siekiera",10))
rufus.wypisz_ekwipunek()
rufus.wypisz_info()
rufus.otrzymaj_obrazenia(100)
rufus.wypisz_info()
rufus.wylecz(300)
rufus.wypisz_info()
rufus.daj_atak()
rufus.otrzymaj_obrazenia(250)
rufus.wylecz(20)
rufus.daj_atak()
rufus.wypisz_info()