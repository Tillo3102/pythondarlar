# import datetime
# import calendar

# hozir = datetime.datetime.now()
# print(hozir)
#
# bugun = datetime.date.today()
# print(bugun)
# print(calendar.calendar(2021))



# file_path = '/home/mirkomil/Documents/ismlar.txt'
# with open(file_path) as file:
#     malumot = file.read()
# print(malumot)



filename = "/home/mirkomil/Documents/cars.txt"
with open(filename, 'w') as file:
    file.write("['audio', 'bmw', 'porchse']")
    file.write("\nYuqoridagi mashinalar listi.")

with open(filename) as file:
    malumot = file.read()

print(malumot)