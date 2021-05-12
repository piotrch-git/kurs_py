#Zadanie #4  patrz na omowienie niżej
class Basket:
    def __init__(self):
        self.zawartosc = []
        self.total_price = 0

    def add_product(self,product,cena_za_produkt):
        self.zawartosc.append(product)
        koszyk1.count_total_price(cena_za_produkt)


    def count_total_price(self,cena_za_produkt):
        self.total_price += cena_za_produkt
        return self.total_price

    def generate_report(self):
        print(self.zawartosc, self.total_price)

koszyk1 = Basket()
koszyk1.add_product("mydło",5)
koszyk1.add_product("kasza",5)

koszyk1.generate_report()
#print(koszyk1.count_total_price())




#Omowienie  # Korzystające z 2ch klas:

class Produkt:
    def __init__(self,id,nazwa,cena):

        self.cena = cena
        self.nazwa = nazwa
        self.id = id

    def wypisz_info(self):
        print(f"Produkt: {self.nazwa} ID: {self.id} Cena: {self.cena}")

class Koszyk:
    def __init__(self):
        self.zawartosc = [] #w tej liście chcemy przechowywać pary (produkt, jego ilosc)

    def element(p,ilosc):
        pass

    def dodaj_produkt(self, p, ilosc=1):
        self.zawartosc.append({"produkt":p, "ilosc":ilosc}) #do listy dodajemy słownik


    def lacznie_cena(self):
        suma = 0
        for slow in self.zawartosc:  #zawartosc zawiera słowniki
            suma += slow["produkt"].cena * slow["ilosc"]            # !
        return suma

    def podsumowanie(self):
        print ("produkty w koszyku")
        for slownik in self.zawartosc:
            print(f"{slownik['ilosc']}x", end="")
            slownik["produkt"].wypisz_info()
        print(f"łączna cena: {self.lacznie_cena(): .2f} PLN")



k = Koszyk()
k.dodaj_produkt(Produkt(1,"woda", 10.00),3)
print(k.lacznie_cena())
k.podsumowanie()