#### date time

import datetime
import calendar




#### Create, read, update, delete


with open('D:/piton/raqamlar2.txt') as file:
    malumot = file.read()

print(malumot)


# filename = "D:/p/cars.txt"
# with open(filename, "w") as file:
#     file.write("['audu','bmw','mers']")

# filename = "D:/p/cars.txt"
# with open (filename) as file:
#     malumot_2 =file.read()


# print(malumot_2)
# filename = "D:/p/cars.txt"
# with open (filename, "d") as file:

# bugun = datetime.date.today()
# print(bugun)

# hozir = datetime.datetime.now()
# print(hozir)

# oy = datetime.month.march() ###ишламади нотугри экан
# print(oy)

# print(calendar.calendar(2021))