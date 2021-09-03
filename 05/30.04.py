# class mahsulot :
#     """
#     Mahsulotlar buyicha
#     """

#     def __init__(self, name, narx):
#         self.name = name
#         self.narx = narx
#         self.soni = 100
#         self.sotildi = 0


#     def tarif (self):
#         print(f"Omborda {self.soni} kg {self.name} bor. Sotuv narhi {self.narx} sum ")

#     def sotuv(self, kg):
#         self.sotildi = kg
#         if self.soni - self.sotildi >= 0:
#             print(f"{self.sotildi} kg {self.name} sotildi")

#     def qoldiq(self):
#         if self.soni - self.sotildi <0:
#             print(f"Omborda {self.sotildi} kg mahsulot mavjud emas")
#         else:
#             qoldiq = self.soni - self.sotildi
#             print(f"Omborda {qoldiq} kg {self.name} qoldi")
    
#     def tushum (self):
#         tushum = self.sotildi*self.narx
#         if self.soni - self.sotildi >=0:
#             print(f"{tushum} sum savdo buldi")

        
# my_mahsulot = mahsulot ("olma", 20000)
# my_mahsulot.tarif()

# my_mahsulot.sotuv(200)
# my_mahsulot.qoldiq()
# my_mahsulot.tushum()

# print()
# yangi_mahsulot = mahsulot("nok", 30000)
# yangi_mahsulot.tarif()
# yangi_mahsulot.sotuv(100)
# yangi_mahsulot.qoldiq()
# yangi_mahsulot.tushum()

# print()
# behi = mahsulot("behi", 50000)
# behi.tarif()
# behi.sotuv(0)
# behi.qoldiq()
# behi.tushum()



##### Try Except
try:

    filename = 'D:/piton/cars.txt'
    with open(filename) as file:
        malumot = file.read()

    except FileNotFoundError:
        with open(filename, "w") as file:
            file.write("['audi', 'bmw', 'porchse'])

    # else:
    #     with open(filename) as file:
    #         malumot = file.read()




   
print(malumot)

