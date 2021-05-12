prawda = True
falsz = False

print(bool("abs")) #jakikolwiek niepusty string daje true"
print(int(True))
print(int(False))

print(f"{2 < 3 =}")
print(f"{2 > 3 =}")
print(f"{2 <= 3 =}")
print(f"{2 >= 3 =}")
print(f"{2 == 3 =}")  #= to przypisanie, == to porównanie
print(f"{2 != 3 =}")

#zadanie
liczba = int(input("podaj liczbę"))
print("większa od 10", liczba > 10)
print("mniejsza równa 15", liczba <= 15)
print("podzielna przez 2:", liczba % 2 == 0)

# Ampersand - &  to jest binarne AND, na bitach po kolei