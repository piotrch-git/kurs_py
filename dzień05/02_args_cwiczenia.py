#join
napis = "ala ma kota"
print(napis.replace("kota", "psa"))
#########

def formatuj(*args, **kwargs):
    napis = '\n'.join(args)
    #napis = napis.replace("$cena",str(kwargs['cena']))
    for klucz in kwargs:  # dla każdego klucza ze słownika robimy zamianę na jego wartość
        napis = napis.replace(f"${klucz}", str(kwargs[klucz]))
    return napis

print(formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=70))
print(formatuj('nazywam się $imie', 'Mam $wiek lat', imie="Jan", wiek=100))