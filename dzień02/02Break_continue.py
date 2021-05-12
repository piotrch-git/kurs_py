i = 0
while i < 10:
    i+= 1
    if i == 2:
        continue #wraca do sprawdzania warunku od początku pętli
    print(i)
    if i == 7:
        break   #całkiem wychodzi z pętli
    print (i)
print("koniec pętli")