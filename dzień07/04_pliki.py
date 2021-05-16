# try:
#     plik = open("plik.txt")
#     print(plik)
# except FileNotFoundError:
#     print("ni ma")


# plik = open("plik.txt")
# print(plik.read())
# plik.close()    #ważne: zamykamy jak już skończymy korzystać

with open("plik.txt") as plik:
    #to jest dobra praktyka. Wewnątrz tego bloku mamy otwarty plik.txt pod zmienną 'plik'. #na końcu on jest automatycznie zamykany więc nie trzeba robić close.
   # print(plik.read()) #zwraca cały plik jako 1 napis
   # print(plik.readlines()) #zwraca listę wierszy
    for wiersz in plik:
        print(wiersz)

#zadanie:
print("zadanie")
try:
    with open("plik.txt") as plik:
        for _ in range(1):
            plik.readline()         #czyta pierwszy wiersz ale nic z nim nie robi
        for i, wiersz in enumerate(plik,1):
            print(f"{i:3}: {wiersz}", end="")  #i:3 to jest formatowanie fstringa że robi 3 znaki odstępu

except FileNotFoundError:
     print("ni ma")

