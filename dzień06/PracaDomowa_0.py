# 0. Do klasy Postac (z zajęć) dodaj atrybut 'atak' (będący liczbą) ustawiany w konstruktorze oraz metodę daj_atak(), która zwróci wartość ataku Postaci.

class Postac:
    def __init__(self, imie, max_zdrowie):
        self.imie = imie
        self.max_zdrowie = max_zdrowie
        self.zdrowie = max_zdrowie
        self.atak = 10

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


rufus = Postac("Zenek", 200)
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