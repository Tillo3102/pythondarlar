class Car:
    """ Oddiy umumiy mashina modeli """
    def __init__(self, firma, model, yil, narx):
        self.firma = firma
        self.model = model
        self.narx = narx
        self.yil = yil
        self.masofa = 0

    def tarif(self):
        print(f"{self.model} made by {self.firma} in {self.yil}. The cost is {self.narx}")

    def masofani_korsat(self):
        print(f"Bu mashina {self.masofa} yurgan.")
    
    def masofani_ornat(self, km):
        self.masofa = km



class Battery:
    """ Umumiy batareya modeli """
    def __init__(self, batareya_quvvati=75):
        self.batareya_quvvati = batareya_quvvati
    
    def batareya_tarif(self):
        print(f"Bu model {self.batareya_quvvati} watt quvvatga ega")

    def batareya_klas(self):
        if self.batareya_quvvati >= 100:
            print("Bu mashina batareyasi A class")
        else:
            print("BU mashina batareyasi B class")


class ElectricCar(Car):
    """ Electromobil modeli """

    def __init__(self, firma, model, yil, narx):
        super().__init__(firma, model, yil, narx)
        self.batareya = Battery(100)




my_car = ElectricCar("tesla", "x3", "2020", 30_000)
my_car.tarif()
my_car.batareya.batareya_tarif()
my_car.batareya.batareya_klas()