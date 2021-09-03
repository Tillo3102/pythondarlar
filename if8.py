number=67
ism=input("Ismingizni kiriting: ")
tugilgan_sana = int(input("\n1 dan 30 gacha bo'lgan raqamlardan o'zingizga yoqqanini kiriting: "))
running = True
while running:
    if tugilgan_sana >= 1 and tugilgan_sana <= 30:
        print()
        running = False
    else:
        print(f"\n{ism.title()} iltimos 1 dan 30 gacha bo'lgan raqamlardan kiritsangiz")
        tugilgan_sana = int(input("Raqamni qayta kiriting: "))
else:
    urinish = int(input("Shartni nechta urinishda bajarmoqchisiz: "))

if tugilgan_sana*urinish>=200:
    number = tugilgan_sana*urinish//6+1
elif tugilgan_sana*urinish>=100:
    number = tugilgan_sana*urinish//4+3
elif tugilgan_sana*urinish<=10:
    number = tugilgan_sana*urinish*3+7
else:
    number = tugilgan_sana*urinish//2+9

# print(number)
print(f"\n{ism.title()}. Biz xozir sizni insonlar fikrini o'qiy olish qobilyatingizni sinab ko'ramiz.\n{ism.title()} siz dasturchi o'ylagan raqamni topishingiz kerak bo'ladi.")
for r in range(1,urinish+1):
    # if r==6:
    #    print()
    #    print(f"{ism.title()} siz so'nggi {r-1}-imkoniyatdan ham foydalana olmadingiz. \nKeyinroq urinib ko'ring. ")
    #    break 
    guess=int(input("\n1 dan 200 gacha bo'lgan oraliqda raqam kiritishingizni tavsiya qilamiz: "))
    if guess != number and r == urinish:
        print("\nNotog'ri")
        print(f"{ism.title()} siz {r}-imkoniyatdan ham foydalana olmadingiz. \nTo'g'ri javob {number} edi.\nQayta urinib ko'ring.")
        break
    elif guess==number:
        print()
        print("\nTabriklaymiz, siz to'g'ri raqamni kiritdingiz!!!")
        print(f"\nSiz topshiriqni {r} urunishda bajardingiz")
        break
    elif guess<number/2:
        print("\n\nNoto'g'ri, yashirilgan raqam siz kiritgan raqamdan 2 martadan ham ko'proq kattaroq, boshqa raqam kriting")
    elif guess<number:
        print("\n\nNoto'g'ri, yashirilgan raqam siz kiritgan raqamdan biroz kattaroq, boshqa harakat qilib ko'ring")
    elif guess/2>number:
        print("\n\nNoto'g'ri, yashirilgan raqam siz kiritgan raqamdan 2 martadan ham ko'proq kichikroq, boshqa raqam kriting")
    else:
        print("\n\nNoto'g'ri, yashirilgan raqam biroz kichikroq, boshqa raqam kriting")
else:
    print(f"\n{ism.title()} siz boshqalardan yaxshiroq natijaga erishdingiz")
print("\nKatta rahmat!!!")