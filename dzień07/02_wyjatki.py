class MojWyjatek(Exception):
    pass

while True:     #przykład pętli i wyjątku
    try:
        x = int(input("Podaj liczbę: "))
        break
    except ValueError:
        print("to nie jest liczba")


try:
    a = int(input())
    b = int(input())
    print(a / b)
    raise MojWyjatek("KOMUNIKAT")

except ZeroDivisionError:
    #ten blok się wykona tylko jezeli kod wewnatrz bloku try zostanie przerwany wyjatkiem typu 'ZeroDivision...'
    print("Nie dziel przez zero")

except ValueError as e: #zapisujemy zadany wyjątek pod zmienną e
    #ten blok się wykona tylko jezeli kod wewnatrz bloku try zostanie przerwany wyjatkiem typu 'ZeroDivision...'
    print("Podaj liczby")
    print("komunikat błędu:",e)

except MojWyjatek:
    print("złapałem Moj Wyjatek")
    raise   #to przepuszcza złapany wyjątek

except:  # pusty except złapie każdy wyjątek. to jest raczej zla praktyka bo nic nie widać, lepiej/bezpieczniej jest definiować konkretne wyjątki ktorych się spodziewamy
    print("nieznany wyjątek")
finally:
    print("to się wykona zawsze")

print("program dalej dziala")
