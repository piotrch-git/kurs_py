class Produkt:
    def __init__(self,id,nazwa,cena):

        self.cena = cena
        self.nazwa = nazwa
        self.id = id

    def __str__(self):                          #teraz można normalnie po ludzku wyprintować tę metodę
        return f"ID:{self.id}, nazwa: {self.nazwa}, cena {self.cena} PLN"

    def wypisz_info(self):
        print(f"Produkt: {self.nazwa} ID: {self.id} Cena: {self.cena}")


p = Produkt(1, "Woda", 10)
#str(p) == p.__str__()
#print(p.__str__())
print(p)


class Osoba:
    def __init__(self,imie, nazwisko, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wzrost = wzrost

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.wzrost}"

    def __lt__(self,other):     #lt - less than
        return self.wzrost < other.wzrost

jan = Osoba("Jan","Kowalski",167)
ania = Osoba("Ania","Nowak",195)

print(jan)
print(ania)

if jan < ania:      #to działa dzięki zdefiniowaniu magicznej metody __lt__ wyżej
    print("Ania jest wyższa")

x = jan + ania #bez sensu, ale to to samo co x = jan.__add__(ania)