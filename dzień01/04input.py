print("napis")
x= input ("podaj dane:")
print("podałeś:", x)
print(x*2)
#Input zawsze jest domyślnie stringiem. Jeżeli to ma być liczba to trzeba to określić

y = int(input("podaj dane:"))
print("podałeś:",y)
print(30*y)

#zadanie
miastoA = input("podaj miasto A:")
miastoB = input("podaj miasto B:")
DystansAB = int(input("podaj dystans AB:"))
cenapaliwa = float(input("podaj cenę paliwa:"))
spalanie = float(input("podaj spalanie:"))
spalonepaliwo = spalanie * DystansAB / 100
koszt = spalonepaliwo * cenapaliwa
print(f"koszt podróży z {miastoA} do{miastoB} to: {koszt:.2f} PLN")  # .2f zaokrągla wynik do 2ch miejscy po przecinku

