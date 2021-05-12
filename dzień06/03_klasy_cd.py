#instancje klas są mutowalne

class Int:
    def __init__(self, x):
        self.x = x

def ustaw3(x):
    x = 3

def ustaw2(arg):
    arg.x = 2

y = 10
ustaw3(y)
print(y)

z = Int(17)
print(z.x)
ustaw2(z)
print(z.x)


#obiekty możemy wykorzystywać wszędzie tam gdzie inne wartości
lista = [Int(3), Int(5), Int(7)]
print(lista)
for i in lista:
    print(i.x)