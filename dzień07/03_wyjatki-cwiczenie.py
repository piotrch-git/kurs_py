#Tu wszystko działa OK

class WithdrawException(Exception):
    pass

class PutException(Exception):
    pass

class CashMachine:
    def __init__(self, limit = 10):
        #self.zawartosc = {}  # zmienna jest publiczna
        # self._zawartosc = {} # _bla to jest konwencja oznaczania zmiennych chronionych (protected) - działa jak publiczna, wylko wywala warning
        self.__zawartosc = {}  # __bla to zmienna prywatna - poza klasą nie jest widoczna
        self.__limit = limit
    def is_available(self):
        return any(map(lambda x: x > 0, self.__zawartosc.values()))

        #Dłuższa wersja:
        # for v in self.zawartosc.values():
        #     if v > 0:
        #         return True
        # return False

    def poka(self):
        print(self.__zawartosc)

    def put_money(self,lista):
        if len(lista) + sum(v for v in self.__zawartosc.values()) > self.__limit:
            raise PutException("Brak miejsca")

        for banknot in lista:
            if banknot in self.__zawartosc:
                self.__zawartosc[banknot] += 1
            else:
                self.__zawartosc[banknot] = 1

    def withdraw_money(self,kwota):
        #podejście 1. Przechodzimy po banknotach od największego nominału i dobieramy dopóki nie uzbieramy kwoty
        nominaly = sorted(self.__zawartosc.keys(), reverse=True)
        wynik = []

        if kwota % 10 != 0:
            raise WithdrawException(f"Nie udało się zebrać kwoty")

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
            raise WithdrawException(f"Nie udało się zebrać kwoty")              #Raise podnosi wyjątek, Except go obsługuje. Tu jest tylko podnoszony wyjątek, on jest obsługiwany pozniej na końcu w interfejsie. #raise jest jak return tylko informuje że coś poszło nie tal

bankomat = CashMachine()

while True:
    op = input("jaką operację chcesz wykonać? wpłać/wypłać/koniec/stan")
    if op == "koniec":
        break
    elif op == "stan":
        bankomat.poka()
    elif op == "wpłać":
        napis = input("podaj wpłacane banknoty rozdzielone spacjami")
        try:
            bankomat.put_money(list(map(int, napis.split())))
        except PutException as e:
            print("Błąd wpłacania", e)
    elif op == "wypłać":
        try:
            kwota = int(input("jaką kwotę chcesz wypłacić?"))
            print("wypłacone banknoty", bankomat.withdraw_money(kwota))
        except WithdrawException as e:
            print("Błąd", e)
        except ValueError:
            print("kwota musi być liczbą całkowitą")




