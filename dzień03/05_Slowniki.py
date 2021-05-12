#Słownik - nieuporządkowoana, mutowalna kolekcja par(klucz - wartość) - od pythona 3.coś gwarantowana jest kolejność zgodna z kolejnością wstawiania
slownik = {}
print(type(slownik))
stan_konta = {"Kowalski":120, "Nowak":15}
print(stan_konta)
print(stan_konta["Kowalski"])
print(type(stan_konta["Kowalski"]))
#print(stan_konta["we"]) # błąd, nie ma takiego klucza
stan_konta["Nowak"] += 10
print(stan_konta)
stan_konta["Duda"] = 1300
print(stan_konta)
stan_konta.pop("Duda")
print(stan_konta)

print(f'{"Nowak" in stan_konta=}')
print(f'{"Duda" in stan_konta=}')

for klucz in stan_konta:    #pętla for przechodzi po kluczach słownika
    print(klucz)

for klucz, wartosc in stan_konta.items():  # slownik.items() zwraca pary klucz-wartość
    print(f"{klucz} => {wartosc}")

    print(list(zip([1,2,3],[10,20,30]))) #sklejanie 2ch list w slownik