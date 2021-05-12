#### tu jest inaczej w tej wersji, nie mamy listy tylko dodatkową klasę pomocniczą

class Produkt:
    def __init__(self,id,nazwa,cena):

        self.cena = cena
        self.nazwa = nazwa
        self.id = id

    def wypisz_info(self):
        print(f"Produkt: {self.nazwa} ID: {self.id} Cena: {self.cena}")

class ElementKoszyka:
    def __init__(self,p,ilosc):
        self.produkt = p
        self.ilosc = ilosc

    def cena(self):
        return self.produkt.cena * self.ilosc

    def wypisz(self):
        print(f"{self.ilosc}x", end="")
        self.produkt.wypisz_info()

    def zawiera_produkt(self, p):
        return self.produkt.id == p.id  #jeżeli id jest takie same to jest to ten sam produkt

    def zwieksz_ilosc(self,n):
        self.ilosc += n

class Koszyk:
    def __init__(self):
        self.zawartosc = [] #w tej liście chcemy przechowywać pary (produkt, jego ilosc)


    def dodaj_produkt(self, p, ilosc=1):
        if isinstance(p, Produkt): #sprawdzamy czy p jest typu produkt lb po nim dziedziczy

            for elem in self.zawartosc:
                if elem.zawiera_produkt(p):     #jeżeli już zawiera produkt to zwieksza jego ilosc
                    elem.zwieksz_ilosc(ilosc)
                    return
            self.zawartosc.append(ElementKoszyka(p, ilosc))      #nie znalezlismy produktu więc dodajemy
        else:
            print("daj mi Produkt")

    def lacznie_cena(self):
        suma = 0
        for elem in self.zawartosc:  #zawartosc zawiera słowniki
            suma += elem.cena()            # !
        return suma

    def podsumowanie(self):
        print ("produkty w koszyku")
        for elem in self.zawartosc:
            elem.wypisz()
        print(f"cana łączna: {self.lacznie_cena()} PLN")



k = Koszyk()
#woda = Produkt(1,"Woda", 10)

k.dodaj_produkt(Produkt(1,"woda", 10.00),2)
k.dodaj_produkt(Produkt(2,"lizak", 1.00),2)
k.dodaj_produkt(Produkt(1,"woda", 10.00),1)


k.podsumowanie()