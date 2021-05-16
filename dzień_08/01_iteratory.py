#klasa jest iterowalna kiedy posiada magiczną metodę __iter__()
#obiekt zwrócony przez __iter__() musi posiadać magiczną metodę __next__()

# lista = [1, 2, 3]
# iterator = iter(lista) #iter(x) woła x.iter__()
# print(iterator)
# print(next(iterator)) #iter(x) woła x.next__()

class Iter:
    def __iter__(self):  #metoda iter ma zwrócić coś co zawiera metodę __next__()
        print("metda __iter__()")
        self.licznik = 3
        return self

    def __next__(self):          #__next__ się w kółko wykonuje dopoki nie ma warunku na stopIteration
        print("metoda __next__()")
        if self.licznik == 0:
            raise StopIteration
        self.licznik -= 1
        return 123


x = Iter()

for i in x:
    print(i)


# it = iter(x)
#
# print(next(it))



it = iter(x)


#Zadanie


class Counter:
    def __iter__(self):
        self.licznik = 0
        return self

    def __next__(self,limit=10):
        if self.licznik == limit:
            raise StopIteration
        self.licznik += 1
        return self.licznik

c = Counter()

for i in c:
    print(i)


#omowienie:

class Counter:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.next_value = 0
        return self
    def __next__(self):
        if self.next_value ==self.limit:
            raise StopIteration
        result = self.next_value
        self.next_value += 1
        return result

for i in Counter(5):
    print(i)


#Zadanie2: omowienie:


class Vowels:
    def __init__(self, napis):
        self.napis = napis

    def __iter__(self):
        self.idx = 0 # idx jest indeksem nastepnego znaku do sprawdzenia
        return self

    def __next__(self):
        while self.idx < len(self.napis):
            litera = self.napis[self.idx]
            self.idx += 1
            if litera.lower() in "aeiouy":
                return litera
        raise StopIteration

for char in Vowels('ala ma kota'):
    print(char)