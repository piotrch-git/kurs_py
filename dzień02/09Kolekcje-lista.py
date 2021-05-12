# w liście elementy mogą być różnego typu
# lista jest obiektem mutowalnym (może się zmieniać)

pusta_lista = [] # listy zawsze w nawiasach kwadratowych
niepusta_lista = [1, 2, 3, 4, "napis", [1,2]] # ta lista ma 6 elementów
print(pusta_lista)
print(niepusta_lista)

print(f"{len(pusta_lista)=}")
print(f"{len(niepusta_lista)=}")

# odwołanie się do n-tego elementu - lista[n] - liczone od 0
print(f"{niepusta_lista[4]=}")
print(f"{niepusta_lista[5][0]=}")   #0wy element 5-tego elementu

print(f"{niepusta_lista[-1]=}") #ostatni element

#slicing
print(f"{niepusta_lista[0:3]=}")
print(f"{niepusta_lista[4:]=}")
print(f"{niepusta_lista[:2]=}")

print(f"{niepusta_lista[0:5:2]=}") #3ci argument to co który element wyciągamy (krok)
print(f"{niepusta_lista[0::]=}") # do końca co drugi

# append - dopisuje element do końca listy.
pusta_lista.append(999)
print(f"{pusta_lista=}")

# pop - usuwa ostatni element
pusta_lista.pop()

lista = []
while len(lista)<10:
    lista.append(123)
print(lista)
print(sum(lista)) #suma wszystkich elementów

#zadanie
lista = []
while len(lista) < 7:
    x = int(input("podaj temperaturę"))
    lista.append(x)
print(lista)
print(f"długość listy to:{len(lista)}")
print(f"średnia temp to {sum(lista)/len(lista)}")

a=5
lista.append(a)
print(lista)