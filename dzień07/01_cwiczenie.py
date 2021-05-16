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


class PremiumEmployee(Employee):
    def __init__ (self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def daj_bonus(self, bonus):
        self.bonus += bonus


    def pay_salary(self):
        wyplata = self.czas_pracy * self.stawka + self.bonus
        self.czas_pracy = 0
        return wyplata



jan = Employee("Jan", "Nowak", 100.0)

jan.register_time(5)

print(jan.pay_salary())
print(jan.pay_salary())
print(jan.pay_salary())
jan.register_time(10)  # 2h nadgodzin
print(jan.pay_salary())
print("kaziu")
kazik = PremiumEmployee('Kazik','Kowalski',100.0)
kazik.register_time(5)
kazik.daj_bonus(5)
kazik.daj_bonus(5)
print(kazik.pay_salary())

print("******* Omowienie ********")



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


class PremiumEmployee(Employee):
    def __init__ (self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def daj_bonus(self, bonus):
        self.bonus += bonus


    def pay_salary(self):
        wyplata = super().pay_salary()
        wyplata += self.bonus
        self.bonus = 0
        return wyplata


jan = PremiumEmployee("Jan", "Nowak", 100.0)
jan.register_time(5)
jan.daj_bonus(5)
print(jan.pay_salary())
print(jan.pay_salary())

