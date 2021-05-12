from random import random   #moduł random zawiera funkcję random.
# Random zwraca losowego floata z przedziału [0.0; 1.0) - prawy nawias 1.0 nie należy do zbioru, a [ należy
#math.hypot(coordinates) - dlugość odcinka



# Działa!

punkty_w_kole = 0
punkty_wszystkie = 0
i = 0
while i < 100000:

    x = random() * 2.0  # losowy float z przedziału [0.0; 2.0)
    y = random() * 2.0
    odleglosc_od_srodka = ((x -1)**2 + (y-1)**2) ** 0.5 # z pitagorasa

    print(f"odleglość od środka{odleglosc_od_srodka}")
    if odleglosc_od_srodka <= 1:
        punkty_w_kole += 1
    punkty_wszystkie += 1
    i += 1

wynik = punkty_w_kole * 4 / punkty_wszystkie

print(wynik)

