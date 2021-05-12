class Auto:
    def __init__ (self, marka,spalanie):
        self.marka = marka
        self.spalanie = spalanie
        self.przebieg = 0

    def przejazd(self, trasa):
        self.przebieg += trasa
        return self.przebieg

samochod = Auto("Toyota",10)
print(samochod.przejazd(100))
print(samochod.przejazd(100))
print(samochod.przejazd(100))



class Lodowka:
    def __init__ (self):
        self.zawartosc = []

    def zaladuj(self,produkt):
        self.zawartosc.append(produkt)
        return self.zawartosc

    def zjedz(self,produkt):
        self.zawartosc.remove(produkt)
        return self.zawartosc
l1 = Lodowka()
print (f"zawartość lodówki = {l1.zawartosc}")
print (f"{l1.zaladuj('jajka')=}")
print (f"{l1.zaladuj('jogurt')=}")
print (f"{l1.zaladuj('maslo')=}")
print (f"{l1.zjedz('jogurt')=}")


