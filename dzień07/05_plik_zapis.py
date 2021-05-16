with open("plik2.txt", 'w') as plik:
    napis = input("co zapisać w pliku?")
    plik.write(napis)
    plik.write('\n')
    plik.write("Ala ma kota")

with open("arkusz.csv", 'w') as plik:  #w - to plik otwarty do zapisu
    plik.write("imię;nazwisko\n")
    plik.write("Jan;Kowalski\n")
    plik.write("Zenek;Burczymucha\n")