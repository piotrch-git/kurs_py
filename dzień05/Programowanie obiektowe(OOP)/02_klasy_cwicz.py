class Employee:
    def __init__ (self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.czas_pracy = 0

    def register_time(self, czas):
        if czas > 8:
            self.czas_pracy += 8 + 2 * (czas - 8)
        else:
            self.czas_pracy += czas

    def pay_salary(self):
        wyplata = self.czas_pracy * self.stawka
        self.czas_pracy = 0
        return wyplata

jan = Employee("Jan", "Nowak", 100.0)

jan.register_time(5)
jan.register_time(5)

print(jan.pay_salary())
print(jan.pay_salary())
print(jan.pay_salary())
jan.register_time(10)  # 2h nadgodzin
print(jan.pay_salary())



