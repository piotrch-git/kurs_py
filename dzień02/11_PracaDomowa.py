#1. Przyjmij 2 liczby N i K, a nastepnie wypisz czy N jest podzielne przez K.

#2. Przyjmij 3 liczby reprezentujace dlugosci odcinkow i wypisz czy da sie z tych odcinkow zbudowac trojkat.

#3. Przyjmij liczbe N i wypisz jej sume cyfr.

#4. Przyjmij 2 liczby A i B, a nastepnie wypisz ile rozwiazan ma rownanie 0 = Ax + B.
#Jesli ma dokladnie jedno to wypisz ile wynosi.

#5. Wczytujemy liczbe naturalna N_1, a nastepnie przeksztalcamy ja w liczbe N_2 w taki sposob, ze N_2 jest suma cyfr liczby N_1.
#Na przyklad dla N_1 = 5839 mamy N_2 = 5 + 8 + 3 + 9 = 25.
#Tak otrzymana wartosc N_2 przeksztalcamy w N_3 wedlug tego samego algorytmu (suma cyfr poprzedniej liczby daje nam nowa liczbe), i tak dalej.
#Ile razy musze dokonac takiego przeksztalcenia, aby uzyskac liczbe jednocyfrowa?
#Np. dla liczby 5839 odpowiedz brzmi: 2, ale dla liczby 1232 odpowiedz brzmi: 1.

#6. Napisz program, ktory przyjmie 10 liczb calkowitych i wypisze z nich najpierw parzyste, a potem nieparzyste.



###################################################
print("zad.1")
###################################################
n = int(input("podaj liczbę N: "))
k = int(input("podaj liczbę K inną niż 0: "))
if k == 0:
    print("k nie może być 0")
    exit()
elif n % k == 0:
     print(f"{n} jest podzielne przez {k}")
else:
    print(f"{n} nie jest podzielne przez {k}")

###################################################
print("zad.2")
###################################################
a = int(input("podaj długość odcinka a inną niż 0: "))
b = int(input("podaj długość odcinka b inną niż 0: "))
c = int(input("podaj długość odcinka c inną niż 0: "))
list = [a,b,c]
max = max(list)
list.remove(max)
if sum(list) > max:
    print ("z odcinków a, b i c da się zrobić trójkąt")
else:
    print("z odcinków a, b i c nie da da się zrobić trójkąta")

###################################################
print("zad.3")
###################################################
i = 0
sum = 0
number = input("podaj liczbę: ")
for digit in number:
    digit=int(digit)
    sum = sum + digit
print(f"suma cyfr w tej liczbie to: {sum}")

##alternatywnie:
n = int(input("podaj N: "))
print(n % 10) #sama cyfra jedności
print(n // 10) #cyfra z uciętą cyfrą jedności

suma = 0
while suma > 0:  #chba tak nie jestem pewien
    suma += n % 10
    n //= 10 # to samo co n = n // 10
print(f"suma cyfr wynosi {suma}")

###################################################
print("zad.4")
###################################################
a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))
if a == 0:
    if b == 0:
        print("jest nieskończenie wiele rozwiązań")
    else:
        print("nie ma rozwiązań")
else:
    print("jest jedno rozwiązanie", -b / a)

###################################################
print("zad.5")
###################################################
number = input("podaj liczbę naturalną: ")
i = 0
while len(number) > 1:  #prościej: while number > 9
    sum = 0
    for n in number:
        n = int(n)
        sum = sum + n
    number = sum
    number = str(number)
    print(i)
    print(number)
    i +=1
print(f"Przekształcenie należy wykonać {i} razy")

#alternatywnie:

n = int(input("podaj n"))
licznik = 0
while n > 9: #dopóki n nie jest jednocyfrowe
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    n = suma

    licznik += 1
print (licznik)



###################################################
print("zad.6")
###################################################
i=1
list = []
even = []
odd = []
while i <= 10:
    l = int(input(f"podaj liczbę całkowitą #{i}: "))
    list.append(l)
    i += 1
for i in list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"liczby parzyste: {even}")
print(f"liczby nieparzyste: {odd}")
