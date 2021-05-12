# 1. Stwórz klasę Przedmiot, który będzie posiadał nazwę i jakiś bonus liczbowy (np. Przedmiot("Kij", 4) => Przedmiot o nazwie "Kij" i bonusie 4) oraz będzie posiadał sensowną reprezentację napisową (metoda __str__()).
class Przedmiot:
    def __init__(self,nazwa,bonus):
        self.nazwa=nazwa
        self.bonus=bonus
    def __str__(self):
        return f"{self.nazwa=},{self.bonus=}"

cos = Przedmiot("kij",4)
print(cos)