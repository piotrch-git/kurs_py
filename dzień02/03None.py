x = None    # kiedy nie chcemy nic przypisywać do zmiennej
print(x)
print(type(x))

if x is None: #operator porownania == sprawdza czy elementy są takie same. Is sprawdza czy elementy są TE same.
    print("x jest puste")

if x is not None:
    print("x jest niepuste")

#zadanie , niedokończone
max = None
min = None
while True:
    liczba = input("podaj liczbę")
    if liczba == "koniec":
        break
    liczba = int(liczba)

    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba
print(f"max to {max}")
print(f"min to {min}")