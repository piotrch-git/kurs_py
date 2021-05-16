# to miałem okej

class Przedmiot:
    def __init__(self,nazwa,bonus):
        self.nazwa=nazwa
        self.bonus=bonus
    def __str__(self):
        return f"{self.nazwa=},{self.bonus=}"

p = Przedmiot("kij",4)
print(p)