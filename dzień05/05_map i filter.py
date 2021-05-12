def podzielne2(x):
    return x % 2 == 0

def dodaj3(x):
    print("dodaję 3")
    return x + 3

print(list(filter(podzielne2, [1,2,3,4])))  #działa jak nasze 'wybierz'

print(list(map(dodaj3, [1,2,3,4])))  #działa jak nasza 'zaaplikuj'

napis = "1 2 3 18 29"
lista_intow = list(map(int, napis.split()))    #sprytna zamiana napisu w listę intów



print(f"{(lambda x: x % 3 == 0)(21) = }")   # lambda definiuje anonimową (bez przypisania nazwy funkcę, która zwraca informację czy liczba jest podzielna przez 3

podzielne_przez_3 = lambda x: x % 3 == 0

for x in filter(podzielne_przez_3, lista_intow):
    print("-",x)

for x in filter(lambda x: x % 5 == 0, lista_intow):
    print("=", x)

##################
dodaj = lambda x, y: x + y  # fkcja przyjmująca 2 argumenty i zwracająca ich sumę
print(f"{dodaj(3,5) = }")