from data import products

class Maxsulot:
    """ Umumiy maxsulot modeli """
    def __init__(self, nomi, narxi, miqdor):
        self.nomi = nomi
        self.narxi = narxi
        self.miqdor = miqdor

    def tarif(self):
        return f"{self.nomi}-{self.narxi} so'm, mavjud-{self.miqdor} kg"
    
    def sotildi(self, kg):
        self.miqdor -= kg

    def qoshish(self, kg):
        self.miqdor += kg



def mavjud_maxsulotlar(data):
    print()
    for id, info in data.items():
        m = Maxsulot(info["nomi"], info["narx"], info["miqdor"])
        print(f"{id}.{m.tarif()}")


def savdo():
    m_id = input("\nMaxsulotni tanlang: ")
    hozirgi_maxsulot = Maxsulot(products[m_id]["nomi"], products[m_id]["narx"], products[m_id]["miqdor"])
    print()
    print(hozirgi_maxsulot.tarif())

    harid_miqdori = float(input(f"Qancha {hozirgi_maxsulot.nomi} olasiz? "))
    if harid_miqdori > hozirgi_maxsulot.miqdor:
        print("Buncha maxsulot mavjud emas.")
        return 0
    else:
        hozirgi_maxsulot.sotildi(harid_miqdori)
        products[m_id]["miqdor"] -= harid_miqdori
        ruyxat = f"{id}:{m_id['nomi']}"
        return harid_miqdori * hozirgi_maxsulot.narxi

def run():
    print("Bizning do'konimizga hush kelibsiz!")
    jami_tolov = 0
    savatcha = []

    while True:
        mavjud_maxsulotlar(products)
        jami_tolov += savdo()
        print(f"\nHozirgi tolov: {jami_tolov} so'm\n")
        davom = input("\nYana harid qilasizmi(ha/yoq) ")
        if davom == "yoq":
            print(f"Sizning jami to'lovingiz {jami_tolov} so'm.")
            print("Xaridingiz uchun raxmat")
            break

run()