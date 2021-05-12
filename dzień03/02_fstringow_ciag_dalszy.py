print(f"{1.23434:.2f}")    #zaokrąglanie do n miejsc po przecinku
x = 12
print(f"{x:3}") # x ma zająć co najmniej 3 znaki, jeżeli jest za krótki to zostaną dostawione spracje z lewej strony

for i in (1,12, 123, 1234, 12345):
    print(f"{i:5}")

x = 1
print(f"{x:4}")  # domyślnie uzupełnia puste znaki w lewą stronę
print(f"{x:<4}") # uzupełnia puste znaki w prawą stronę
print (f"{x:_<4}") # uzupełnia puste znaki określonym symbolem (tutaj: _)

#zadanie #5:
print("#####zadanie")
print(" " * 3, end="") # 3 spacje przed pierwszym rzędem
for i in range(10):
    print(f"{i:3}",end="")
print()
for x in range (10):
    print(f"{x:<3}", end="")
    for y in range(10):
        wynik = x * y
        print(f"{wynik:3}", end="")
    print()

# albo to samo ale zparametryzowany spacing:
print("#####zadanie ze spacingiem w zmiennej")
s = 4
print(" " * s, end="") # 3 spacje przed pierwszym rzędem
for i in range(10):
    print(f"{i:{s}}",end="")
print()
for x in range (10):
    print(f"{x:<{s}}", end="")
    for y in range(10):
        wynik = x * y
        print(f"{wynik:{s}}", end="")
    print()
