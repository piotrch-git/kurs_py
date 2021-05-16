class Postac:
    def __init__(self, imie, max_zdrowie, atak):
        self.imie = imie
        self.max_zdrowie = max_zdrowie
        self.zdrowie = max_zdrowie
        self.atak = atak

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



rufus = Postac("Rufus",100,4)
rufus.wypisz_info()
rufus.otrzymaj_obrazenia(13)
rufus.wypisz_info()
rufus.wylecz(120)
rufus.wypisz_info()
rufus.otrzymaj_obrazenia(130)
rufus.wylecz(20)