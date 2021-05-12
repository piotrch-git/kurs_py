#*8. Napisz funkcję, która sprawdzi czy podany napis jest wyrażeniem nawiasowym. Tym razem napis może zawierać dowolne nawiasy (tj. okrągłe '()', kwadratowe '[]', klamrowe '{}' oraz ostre '<>'). Oczywiście nawias zamykający zamyka tylko odpowiadający mu nawias otwierający, tzn. '[)' *nie* jest poprawnym wyrażeniem, ale '[(){<>}]' jest. (hint do zadania: https://pl.wikipedia.org/wiki/Stos_(informatyka) - może się przydać listowa metoda pop())

def wyrażenie_naw_2(napis):
    #()[]
    stos = []
    for znak in napis:
        if znak == '(' or znak == '[':
            stos.append(znak)
        elif znak == ')':
            if stos == [] or stos[-1] != '(':
                return False
            stos.pop()  #usuwamy znak ze stosu
        elif znak == ']':
            if stos == [] or stos[-1] != '[':
                return False
            stos.pop()  #usuwamy znak ze stosu
    return stos == []   # jeżeli stos jest pusty (wszystkie otwarte nawiasy zostały zamknięte, zwraca true
print(f"{wyrażenie_naw_2('[(])') = }")
print(f"{wyrażenie_naw_2('[]()') = }")
print(f"{wyrażenie_naw_2('[()') = }")


# uproszczenie kodu za pomocą słownika: (łatwiej też dodawać więcej nawiasów)

def wyrażenie_naw_2(napis):
    #()[]
    nawiasy = {')': '(', ']':'[','}':'{'}
    stos = []
    for znak in napis:
        if znak in nawiasy.values(): # czy znak jest nawiasem otwierającym
            stos.append(znak)
        elif znak in nawiasy:
            if stos == [] or stos[-1] != nawiasy[znak]:
                return False
            stos.pop()


    return stos == []   # jeżeli stos jest pusty (wszystkie otwarte nawiasy zostały zamknięte, zwraca true
print(f"{wyrażenie_naw_2('[(])') = }")
print(f"{wyrażenie_naw_2('[]()') = }")
print(f"{wyrażenie_naw_2('[()') = }")
print(f"{wyrażenie_naw_2('[()]{}') = }")