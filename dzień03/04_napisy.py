# napisy są uporządkowanlnymi, niemutowalnymi (tak jak tupla) zbiorami znaków.

napis = "alamakota"
print(napis[3])
print(type(napis[3]))
print(napis[2:6])
print(f"{'lama' in napis=}")  # in dla napisów zwraca informację czy zadany podciąg występuje w napisie
print(f"{'lama' in list(napis)=}")  # in dla list zwraca informację czy zadany element występuje w liście
print(napis.lower())
print(napis.upper())
print(napis.capitalize())
print(napis.replace("kota","psa"))

#napis[3] = "A"  #to nie działa - niemutowalność!

napis += "heh"  # to działa - to nie jest zmiana tylko sklejenie
print (napis)

#########
#zła praktyka:
k = ""
x = k
for _ in range(1000000):
#    k+= "A"     # - odradza się korzystanie z operatora += przy sklejaniu napisów. Bo to bardzo spowalnia
    x = k
print(k)

######
#dobra praktyka: 'join'
napisy = []
for i in range(10):
    napisy.append("A")
print(napisy)
print("_".join(napisy)) #join skleja ze sobą napisy

##################################
#zadanie 7
print("zadanie7")

samogloski = "aeiouy"
napis = input("podajnapis") #nie trzeba konwertowąc bo input zawsze zwraca stringa
liczba_samoglosek = 0
for i in napis:
    if i.lower() in samogloski:  #bez lower nie zliczy dużych samoglosekA
        liczba_samoglosek +=1
print (f"{liczba_samoglosek=}")


###### zadanie8
#niechlujne rozwiązanie na szybko:
napis = input("podajnapis1")
x = 0
for i in napis:
    if i == '<':
        start=x
    if i == '>':
        stop=x
    x += 1

print(start)
print(stop)
print(stop-start-1)

#lepsze rozwiązanie:
napis = input("podajnapis2")
min = 0
max = 0
for idx, znak in enumerate(napis):
    if znak == "<":
        min = idx
    elif znak == ">":
        max = idx
print(max-min-1)

#inne rozwiązanie:
napis = input("podajnapis3")
min = napis.index("<")
max = napis.index(">")
print(max-min-1)

#inne rozwiązanie:
napis = input("podajnapis4")
for idx, znak in enumerate(napis):
    if znak == "<":
        min = idx
    elif znak == ">":
        max = idx
print(max-min-1)



#najlepsze rozwiązanie:
napis = input("podajnapis5")
licznik = 0
wewnatrz_nawiasu = False #zmienna boolowska
for znak in napis:
    if znak =="<":
        wewnatrz_nawiasu = True
    elif znak ==">":
        wewnatrz_nawiasu = False
        break       # bo jest założenie że jest tylko jedna para nawiasów
    elif wewnatrz_nawiasu:
        licznik += 1
print (licznik)