# **5. Napisz klasę Zolw, która będzie przechowywała informację o położeniu żółwia na płaszczyźnie (2 liczby _rzeczywiste_) oraz kierunku wyrażonym w stopniach, w którym jest zwrócony.
# 	Zolw powinien udostępniać metody:
# 		- wypisz() - wypisuje położenie i zwrot żólwia,
# 		- lewo(n) - obraca żółwia o n stopni w lewo,
# 		- prawo(n) - obraca żółwia o n stopni w prawo,
# 		- naprzod(n) - przemieszcza żółwia o n jednostek w kierunku, w którym obecnie jest zwrócony.
# 	Hint do zadania: `import math` i trygonometria. ;)

import math

class zolw:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.zwrot = 0

