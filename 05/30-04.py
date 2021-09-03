# class Maxsulot:
#     def __init__(self, nomi, narxi):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.miqdor = 100

#     def tarif(self):
#         print(f"{self.nomi} {self.narxi} so'm turadi.Hozirda {self.miqdor} kg mavjud.")

#     def sotildi(self, kg):
#         self.miqdor -= kg

# meva_1 = Maxsulot("Olma", 12000)
# meva_1.tarif()

# meva_1.sotildi(30)
# meva_1.tarif()




# def hisobla(a, b):
#     try:
#         natija = a / b
#     except ZeroDivisionError:
#         print("Nolga bo'lib bo'lmaydi.")
#     else:
#         print(natija)

# hisobla(5, 1)

# try:
#     print(10 + "ab")
# except TypeError:
#     print("Songa so'zni qoshma.")



try:
    with open("cars.txt") as file:
        malumot = file.read()
        print(malumot)

except FileNotFoundError:
    with open("cars.txt", 'w') as file:
        file.write("['audi', 'bmw']")


try:
    with open("cars.txt", 'a') as file:
        malumot = file.write("['audi', 'bmw']")
        print(malumot)

except FileNotFoundError:
    with open("cars.txt", 'w') as file:
        file.write("['audi', 'bmw']")