#Zadanie 5 - bankomat

class CashMachine:
    def __init__(self):
        #self.zawartosc = {}  # zmienna jest publiczna
        # self._zawartosc = {} # _bla to jest konwencja oznaczania zmiennych chronionych (protected) - działa jak publiczna, wylko wywala warning
        self.__zawartosc = {}  # __bla to zmienna prywatna - poza klasą nie jest widoczna
    def is_available(self):
        return any(map(lambda x: x > 0, self.__zawartosc.values()))

        #Dłuższa wersja:
        # for v in self.zawartosc.values():
        #     if v > 0:
        #         return True
        # return False

    def put_money(self,lista):
        for banknot in lista:
            if banknot in self.__zawartosc:
                self.__zawartosc[banknot] += 1
            else:
                self.__zawartosc[banknot] = 1

    def withdraw_money(self,kwota):
        #podejście 1. Przechodzimy po banknotach od największego nominału i dobieramy dopóki nie uzbieramy kwoty
        nominaly = sorted(self.__zawartosc.keys(), reverse=True)
        wynik = []
        for nom in nominaly:
            ile = kwota // nom  #ile banknotow potrzebujemy
            if self.__zawartosc[nom] >= ile:
                self.__zawartosc[nom] -= ile
                for _ in range(ile):  # _ to jest legitna wartosc, oznacza że nas nie interesuje co to jest
                    wynik.append(nom)
                kwota -= ile * nom
            else:
                for _ in range(self.__zawartosc[nom]):
                    wynik.append(nom)
                kwota -= self.__zawartosc[nom] * nom
                self.__zawartosc[nom] = 0

        if kwota == 0: #jesli na koniec kwota = 0 to znaczy że uzbieraliśmy szukaną kwotę
            return wynik
        else:       #nie udało nam się zebrać kwoty więc to co nazbierał wraca
            self.put_money(wynik)
            return []

bankomat1 = CashMachine()

print(bankomat1.is_available())
#bankomat1.__zawartosc[13]=20      # dostep do 'zawartosc' nie powinien być legalny. Dlatego mamy hermetyzację (private/public).(__zawartosc)
bankomat1.put_money([100,50])
bankomat1.put_money([100,50])

print(bankomat1.is_available())
print("####")
bankomat1.withdraw_money(300)
print(bankomat1.is_available())
