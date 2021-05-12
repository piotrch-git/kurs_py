#'self' to konwencja, ale może być tak naprawdę cokolwiek (np buga)
class ElectricCar:
    def __init__(self):
        self.battery_level = 100

    def charge(self):
        battery_level = 100
        return battery_level

    def drive(self,range):

        if self.battery_level >= range:
            self.driven = range
        elif self.battery_level < range:
            self.driven = self.battery_level

        self.battery_level -= self.driven

        if self.battery_level < 0:
            self.battery_level = 0

        return self.driven, self.battery_level

car1 = ElectricCar()

print (f"{car1.drive(20)=}")
print (f"{car1.drive(20)=}")
print (f"{car1.drive(100)=}")
print (f"{car1.charge()=}")
print (f"{car1.drive(50)=}")

#omowienie: tutaj podajemy zasieg samochodu jako atrybut klasy na poczatku

class ElectricCar:
    def __init__(self, zasieg):
        self.zasieg = zasieg    #zasieg - aktualny zasieg samochodu
        self.max_zasieg = zasieg

    def drive(self,dystans):

        if dystans < self.zasieg:
            self.zasieg -= dystans
            return dystans
        else:
            wynik = self.zasieg
            self.zasieg = 0
            return wynik


    def charge(self):
        self.zasieg = self.max_zasieg


car1 = ElectricCar(100)

print (f"{car1.drive(20)=}")
print (f"{car1.drive(20)=}")
print (f"{car1.drive(100)=}")
print (f"{car1.charge()=}")
print (f"{car1.drive(50)=}")





