# 6. W klasie Vector (z zajęć) doimplementuj metodę pozwalającą na pomnożenie liczby razy Vector (Vector razy liczba już mamy - metoda __mul__).
# 	Do rozwiązania tego może przydać się zapoznanie ze stroną dokumentacji https://docs.python.org/3/reference/datamodel.html.
# 	Hint: Szukana metoda ma nazwę zaczynającą się na 'r'.


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x} {self.y}>"

    def __add__(self,other):    #v1 + v2 <=> v1.__add__(v2)
        return Vector(self.x + other.x, self.y + other.y)   #zwracamy nowy wektor z dwóch innych


    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self,n):
        return Vector(self.x * n, self.y * n)

    def __rmul__(self,n):
        return Vector(self.x * n,self.y * n)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __lt__(self,other):
        return self.length() < other.length()

vect1 = Vector(5,5)
vect2 = Vector(3,1)
print(vect1)
print(vect2)

print(vect1 + vect2)
print(vect1 - vect2)
print(vect1 * 5)
print(5 * vect1)

print(vect2 < vect1)

