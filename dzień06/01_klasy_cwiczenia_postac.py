class Postac:
    #postać posiada imie i ileś zdrowia / max zdrowie
    def __init__(self, imie, max_zdrowie):
        self.imie = imie
        self.max_zdrowie = max_zdrowie
        self.zdrowie = max_zdrowie

    #wypisuje imie i zdrowie/max zdrowie
    def wypisz_info(self):
        return self.imie, self.zdrowie

    #zwraca info czy postać żyje (nie żyje jeśli zdrowie = 0)
    def czy_zyje(self):
        return self.zdrowie != 0

    #postać otrzymuje dmg obrażeń
    def otrzymaj_obrazenia(self,dmg):
        if self.zdrowie > dmg:
            self.zdrowie -= dmg
            return self.zdrowie
        elif self.zdrowie <= dmg:
            self.zdrowie = 0
            return self.zdrowie


    #postać regeneruje X punktów zdrowia
    #jesli postac nie żyje to leczenie nie daje żadnego efektu
    def wylecz(self, ile):
        if self.zdrowie == 0:
            print("już nie żyjesz, za późno na 1wszą pomoc")
            return self.zdrowie
        self.zdrowie += ile
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = self.max_zdrowie
            return self.zdrowie

ludzik = Postac("Mocarz",100)
print(f"{ludzik.wypisz_info()=}")
print(f"{ludzik.otrzymaj_obrazenia(20)=}")
#print(f"{ludzik.otrzymaj_obrazenia(20)=}")
#print(f"{ludzik.otrzymaj_obrazenia(20)=}")
print(f"{ludzik.czy_zyje()=}")
print(f"{ludzik.wypisz_info()=}")
print(f"{ludzik.wylecz(10)=}")
print(f"{ludzik.wypisz_info()=}")

print("#####################")
#Omowienie

class Postac:
    def __init__(self, imie, max_zdrowie):
        self.imie = imie
        self.max_zdrowie = max_zdrowie
        self.zdrowie = max_zdrowie

    def wypisz_info(self):
        print(f"{self.imie}, zdrowie: {self.zdrowie}/{self.max_zdrowie}")

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

rufus = Postac("Rufus",100)
rufus.wypisz_info()
rufus.otrzymaj_obrazenia(13)
rufus.wypisz_info()
rufus.wylecz(120)
rufus.wypisz_info()
rufus.otrzymaj_obrazenia(130)
rufus.wylecz(20)