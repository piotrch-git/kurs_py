# tupla (lub krotka) jest niemutowalna (w przeciwieństwie do listy)
# tuplę tworzy przecinek (a nie nawiasy)
pusta_tupla = ()
niepusta_tupla = (10, 20, 30, 40)

print(f"{niepusta_tupla[1]=}")
# niepusta_tupla[1] = 123 # to się nie uda - nie można zmieniać tupli po stworzeniu

x = 1.2 # to jest float
y = 1,2 # to jest tupla
print (type(y))

jednoelementowa_tupla = (1) # takie coś to nie tupla tylko wyrażenie arytmetyczne
jednoelementowa_tupla = (1,) # to jest tupla

(a,b) = (10, 20) # to jest zwykłe przypisanie (aka przypisanie tuplowe), a to 10, b to 20
print(a,b)
a, b = b, a # to zamienia wartości tych zmiennych
print(a,b)

#zadanie
tupla = (1,2,3,4,5,6,7,8,9,10)
print(f"oryginalna tupla {tupla}")
print(f"drugi element (z inexem1) {tupla[1]}")
print(f"przedostatni element {tupla[-2]}")
print(f"od 3 do 7 włącznie {tupla[2:7]}")
print(f"co trzeci{tupla[::3]}")
print(f"co drugi od konca {tupla[::-2]}")

