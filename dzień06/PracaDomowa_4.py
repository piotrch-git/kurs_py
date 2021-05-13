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

class Robot:
    def __init__(self):
        self.x=0
        self.y=0
        self.zwrot=0
        self.kierunki=["N","E","S","W"]


    def wypisz(self):
        print(self.x,self.y,self.kierunki[self.zwrot % 4])

    def prawo(self):
        self.zwrot += 1

    def naprzod(self):
        if self.zwrot % 4 == 0:
            self.y += 1
        elif self.zwrot % 4 == 1:
            self.x += 1
        elif self.zwrot % 4 == 2:
            self.y -= 1
        elif self.zwrot % 4 == 3:
            self.x -= 1

    def lewo(self):
        self.zwrot -= 1

    def wykonaj(self,instrukcje):
        for i in instrukcje:
            if i == "P":
                self.prawo()
            elif i == "L":
                self.lewo()
            elif i == "N":
                self.naprzod()

Robi = Robot()
Robi.wypisz()
Robi.wykonaj("NNPNLNPP")
Robi.wypisz()
