from bir_class import ElectricCar, Battery, Car
# from bir import *

my_car = ElectricCar("tesla", "x3", "2022", 30_000)
my_car.tarif()
my_car.batareya.batareya_tarif()
my_car.batareya.batareya_klas()


said_car = ElectricCar("audi", "A7", "2020", 21000)

said_car.tarif()

said_battary = Battery(100)
said_battary.batareya_tarif()
said_battary.batareya_klas()

said_car = Car("Audi","A700", 2021, 40000)
said_car.tarif()


