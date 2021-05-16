#zadanie z logami (wg omowienia)

with open ("logs.txt") as plik:
    wiersze = plik.readlines()

czas_ostatniego_logowania = {}
laczny_czas = {}
for w in wiersze:
    nazwa_uzytkownika, rodzaj_operacji, czas = w.split(';')
    czas = int(czas)
    if rodzaj_operacji == "LOGIN":
        czas_ostatniego_logowania[nazwa_uzytkownika] = czas
    elif rodzaj_operacji == "LOGOUT":
        czas_sesji = czas - czas_ostatniego_logowania[nazwa_uzytkownika]

        if nazwa_uzytkownika in laczny_czas:
            laczny_czas[nazwa_uzytkownika] += czas_sesji
        else:
            laczny_czas[nazwa_uzytkownika] = czas_sesji


for user, czas in sorted(laczny_czas.items(), key=lambda x: x[1]):
    print(f"{user}: {czas}s")


