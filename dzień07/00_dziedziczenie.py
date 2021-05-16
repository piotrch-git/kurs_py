class Zwierz:
    def __init__(self, imie):
        self.imie = imie

    def daj_glos(self):
        print(f"{self.imie}: ??")

    def daj_imie(self):
        return self.imie

class Pies(Zwierz):  # to oznacza że Pies dziedziczy po Zwierzu, albo inaczej " Pies is a Zwierz"

    def __init__(self, imie, rasa):
        super().__init__(imie)  #super daje nam dostęp do metod nadklasy nawet kiedy są one przysłonięte(nadpisane)  # ten konstruktor z psa to cały konstruktor ze zwierzęcia + dodatkowe argumenty (np.rasa)
        self.rasa = rasa

    def daj_glos(self):         #ta metoda nadpisuje metodę daj_glos z klasy Zwierz (bo pies dziedziczy po zwierz)
        print(f"{self.imie}: Hau!")

    def aport(self):    #to jest metoda tylko psa.
        print("Woof")

p = Pies("Burek", "buldog")
print(p.daj_imie())
print(p.daj_glos())

z = Zwierz("ZZ")
print(f"{isinstance(z, Zwierz) = }") # czy 'z' jest typu 'Zwierz'
print(f"{isinstance(z, Pies) = }")
print(f"{isinstance(z, Zwierz) = }")    #to też jest true, bo isinstance odpowiada na pytanie czy jest teggo typu lub czy dziedziczy po tym typie.
print(f"{isinstance(p, Pies) = }")
#gdy wywołujemy metodę na obiekcie klasy to sprawdzamy po kolei:
#1. czy ta klasa zawiera metodę o takiej nazwie - jeśli tak to ją wywołujemy jeśli nie to:
#2 . czy nadklasa (klasa po ktorej dziedziczymy) zawiera metodę o takiej nazwie - jeśli tak to ją wywołujemy. Jeśli nie to błąd.