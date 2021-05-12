# 0. Do klasy Postac (z zajęć) dodaj atrybut 'atak' (będący liczbą) ustawiany w konstruktorze oraz metodę daj_atak(), która zwróci wartość ataku Postaci.
#
# 1. Stwórz klasę Przedmiot, który będzie posiadał nazwę i jakiś bonus liczbowy (np. Przedmiot("Kij", 4) => Przedmiot o nazwie "Kij" i bonusie 4) oraz będzie posiadał sensowną reprezentację napisową (metoda __str__()).
#
# 2. Rozszerz klasę Postać (zad 0.) o ekwipunek - dodaj metody:
# 	- daj_przedmiot(p) - dodaje Przedmiot(zad 1.) do ekwipunku,
# 	- wypisz_ekwipunek - wypisuje wszystkie Przedmioty posiadane przez daną Postać.
#
# 3. W klasie Postać (zad 0.) zmodyfikuj metodę daj_atak(), żeby zwracała wartość ataku Postaci powiększoną o sumę bonusów z posiadanych w ekwipunku(zad 2.) Przedmiotów(zad 1.).
#
# 4. Wyobraźmy sobie robota, który może poruszać się naprzód i obracać w lewo lub prawo o 90 stopni.
# 	Napisz klasę Robot, która będzie przechowywała informację o położeniu robota na płaszczyźnie (2 liczby całkowite) oraz
# 	kierumku w jakim jest zwrócony (N - północ, S - południe, E - wschód, W - zachód).
# 	Klasa powinna udostępniać metody:
# 		- wypisz() - wypisuje położenie i zwrot robota,
# 		- lewo() - zmienia kierunek, w którym zwrócony jest Robot o 90 stopni w kierunku przeciwnym do ruchu wskazówek zegara (np. N zamieniamy na W),
# 		- prawo() - zmienia kierunek, w którym zwrócony jest Robot o 90 stopni w kierunku zgodnym z ruchem wskazówek zegara (np. N zamieniamy na E),
# 		- naprzod() - przemieszcza robota krok w kierunku, w którym obecnie jest zwrócony (przykładowo krok na wschód powoduje zmianę współrzędnych z (x, y) na (x + 1, y)),
# 		- wykonaj(ciag_instrukcji), gdzie ciąg instrukcji to napis złożony z liter N, P, L oznaczających odpowiednio: Naprzód, Prawo, Lewo (tzn. instkcja N odpowiada jednemu wywołaniu metody naprzod(), P - prawo(), L - lewo()).
# 			Wywołanie metody wykonaj() powinno przemieścić robota zgodnie z przekazanymi instrukcjami.
# 			Przykład:
# 			- początkowe położenie robota: (0, 0), zwrot: N,
# 			- ciąg instrukcji: NNPNLNPP,
# 			- końcowe położenie robota: (1, 3), zwrot: S.
#
# **5. Napisz klasę Zolw, która będzie przechowywała informację o położeniu żółwia na płaszczyźnie (2 liczby _rzeczywiste_) oraz kierunku wyrażonym w stopniach, w którym jest zwrócony.
# 	Zolw powinien udostępniać metody:
# 		- wypisz() - wypisuje położenie i zwrot żólwia,
# 		- lewo(n) - obraca żółwia o n stopni w lewo,
# 		- prawo(n) - obraca żółwia o n stopni w prawo,
# 		- naprzod(n) - przemieszcza żółwia o n jednostek w kierunku, w którym obecnie jest zwrócony.
# 	Hint do zadania: `import math` i trygonometria. ;)
#
# 6. W klasie Vector (z zajęć) doimplementuj metodę pozwalającą na pomnożenie liczby razy Vector (Vector razy liczba już mamy - metoda __mul__).
# 	Do rozwiązania tego może przydać się zapoznanie ze stroną dokumentacji https://docs.python.org/3/reference/datamodel.html.
# 	Hint: Szukana metoda ma nazwę zaczynającą się na 'r'.
#
# *7. Napisz jak najwygodniejszą w użyciu klasę Ulamek. Z niezbędnych funkcjonalności:
# 	- wypisywanie (print(ulamek)),
# 	- stworzenie ułamka z zerowym mianownikiem powinno być niemożliwe (odpowiedni komunikat i mianownik ustawiony na 1),
# 	- jak najwięcej operatorów arytmetycznych. W szczególności: +, -(również __neg__()), *, /, +=, -=, *=, /= działające zarówno
# 		dla działań z innymi ułamkami jak i z liczbami całkowitymi (int). Gdzie ma to sens operacje powinny działać
# 		nawet jeżeli po lewej stronie działania jest wartość niebędąca ułamkiem (np. 3 * ulamek),
# 	- operatory logiczne: <, <=, >, >=, ==, != działające dla porówniań ułamka z ułamkiem, ułamka z intem i inta z ułamkiem,
# 	- ułamek po każdej operacji powinien być w postaci nieskracalnej (tzn. 1/4 + 1/4 powinno dać w wyniku ułamek 1/2 a nie 2/4).