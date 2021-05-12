#wyznaczanie największej liczby
max = None

while True:
    napis = input("podaj liczbę lub koniec żeby zakończyć")
    if napis == "koniec":
        break
    liczba = int(napis)
    print(f"liczba to {liczba}")

    if max == None or liczba > max:  #w tym OR jeżli pierwszy warunek jest true to drugio nie jest w ogóle sprawdzany, więc może mieś nielegalne porównanie
        max = liczba

if max == "":
    print("nie podałeś liczb")
else:
    print(f"Największa liczba to:{max}")