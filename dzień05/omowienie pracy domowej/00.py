#0. Napisz funkcję, która sprawdzi czy podana lista jest posortowana rosnąco.

def czy_rosnaca(lista):
    for i in range(len(lista)-1):
        if not lista[i] < lista[i+1]:
            return False
    return True
print(f"{czy_rosnaca([1,3,5,4])=}")




