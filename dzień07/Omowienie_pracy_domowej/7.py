
def nwd(a,b):
    if b == 0:
        return a
    return nwd(b,a % b)

class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.ustaw_mianownik(mianownik)
        self.skroc()                        #od razu skraca ulamek przy tworzeniu

    def ustaw_mianownik(self, mianownik):
        if mianownik == 0:
            print("mianownik nie może być 0, ustawiam na 1")
            mianownik = 1
        self.mianownik = mianownik

    def __str__(self):
        return f"({self.licznik}/{self.mianownik})"

    def __mul__(self, other):
        #wyjątek żeby print(a * 5 ) działało
        if isinstance(other, Ulamek):
            return Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)
        if isinstance(other, int):
            return Ulamek(self.licznik * other, self.mianownik)

    def __rmul__(self, other): #other * self gdy other nie wspiera __mul__()    #wyjątek żeby 5 * a działało
        return self * other #tu wywolamy Ulamek.__mul__(), bo self jest typu Ulamek

    def skroc(self):
        n = nwd(self.licznik, self.mianownik)
        self.licznik //= n  # // żeby dawało liczby całkowite bez ulamkow
        self.mianownik //= n

a = Ulamek(2,4)
print(a)

b = Ulamek(2,3)
print(b)

print(a*b) # to samo co a.__mul__(b)

print (a * 5)
print (5 * a)
print(a)