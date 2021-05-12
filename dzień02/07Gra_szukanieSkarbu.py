from random import randint

#x_gracz = randint(0,10)
#y_gracz = randint(0,10)
x_gracz = 0
y_gracz = 0

x_skarb = randint(0,10)
y_skarb = randint(0,10)
i = 0

print (f"startujesz na pozycji {x_gracz}, {y_gracz}")
print (f"skarb jest na pozycji {x_skarb}, {y_skarb}")

while True:
    odleglosc = abs(x_skarb - x_gracz) + abs(y_skarb - y_gracz)
    max_ilosc_ruchow = odleglosc * 2
    print(f"odległość do skarbu to {odleglosc}")
    ruch = input("w którą stronę idziesz? g/d/l/p?")
    if ruch == "g":
        y_gracz += 1
    elif ruch == "d":
        y_gracz -= 1
    elif ruch == "l":
        x_gracz -= 1
    elif ruch == "p":
        x_gracz += 1
    else:
        print("błędny kierunek")
        continue    # żeby nie zliczał nieprawdziwych kroków
    i += 1
    print(f"jesteś na pozycji{x_gracz}, {y_gracz}")
    print(f"skarb jest na pozycji {x_skarb}, {y_skarb}")

    #z prawdopodobieństwaem 1/5 nie podawaj wskazowki ciepło zimno
    if randint(0,5) >=2 :
        if odleglosc < abs(x_skarb - x_gracz) + abs(y_skarb - y_gracz):
            print("zimno")
        elif odleglosc > abs(x_skarb - x_gracz) + abs(y_skarb - y_gracz):
            print("ciepło")

    odleglosc = abs(x_skarb - x_gracz) + abs(y_skarb - y_gracz)

    if x_skarb == x_gracz and y_skarb == y_gracz:
        print(f"znalazłeś skarb! To zajęło {i} ruchów")
        break
    if x_gracz < 0 or y_gracz < 0 or x_gracz > 10 or y_gracz > 10:
        print("wypadłeś za planszę!")
        break
