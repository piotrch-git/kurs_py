
#6. Napisz funkcję, która sprawdzi czy podany napis jest poprawnym wyrażeniem nawiasowym (wyjaśnienie niżej). Zakładamy, że napis zawiera tylko znaki '(' i ')'. (podobną rzecz robiliśmy w zadaniu 3 z funkcji)

# to co napisałem jest zle bo przechodzi takie cos )(

def czy_wyrazenie_nawiasowe(napis):
    licznik = 0
    for znak in napis:
        if znak == '(':
            licznik += 1
        elif znak == ')':       #elif a nie if bo bardziej optymalnie, nie sprawdza elifa jezeli pierwszy if pasuje.
            licznik -= 1
            if licznik < 0:  # to jest naprawienie tego co miałem zle : np. )(()
                return False
    return licznik == 0

print(czy_wyrazenie_nawiasowe('())('))
