
"""
Created on Fri Nov 24 22:00:33 2023

@author: user
"""
"""
sonlar=list(range(11,100,2))
for son in sonlar:
  print(son**3)
  
sev_kitob=input("5 ta sevimli kitoblaringizni kiring")
kitoblar=list(sev_kitob)
for kitob in sev_kitob:
    print(kitob)
"""
"""
kitoblar=[]
print("Sevimli kitoblaringiz ro'yxatini tuzing:")
for n in range(4):
  kitoblar.append(input(f"{n+1}-kitobni kiriting:"))
print(kitoblar)    
"""
"""
odamlar=[]
print("Bugun kimlar bilan uchrashdingiz?")
for k in range(5):
    odamlar.append(input(f"{k+1}-odamni kiriting:"))
print(odamlar)
"""
"""
yangi_cars=['toyota','hyundai','mazda','gm','kia']
for car in yangi_cars:
    if car=='gm':
        print(car.upper())
    else: 
        print(car.title())
"""
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks xolda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
"""
login=input("Foydalanuvchi ismini kiriting:")
if login=="Admin":
    print("Salom Admin xush kelibsiz!")
else:  
    print(f"Salom {login} xush kelibsiz!")
"""
"""
son_1=input("salom! 1-sonni kiriting:")
son_2=input("2-sonni kiriting:")
if son_1==son_2:
    print("2 la son teng ekan!")
else:
    print("Bu sonlar bir- biriga teng emas ekan!")
"""
"""
tarjima_lugat={}
tarjima_lugat["print"]="Konsolga chiqarish"
tarjima_lugat['if']="Agar degan ma'noda va turli shartlarni bajaradi"
tarjima_lugat["string"]='Matnli ifoda yoki qiymat'
tarjima_lugat["float"]="O'nli kasrlar"
kalit=input("Tarjimasini qidirmoqchi bo'lgan so'zingizni kiriting:")
qiymat=tarjima_lugat.get(kalit, "lug'atda mavjud emas")
print(f"{kalit} so'zi {qiymat}!")
"""
"""
python_words = {
    'integer':'Butun son',
    'float': "O'nlik son",
    'boolean':"Mantiqiy qiymat",
    'for':"Biror amalni qayta-qayta bajarish tsikli",
    'if':'Shartlarni tekshirish operatori'}
for w,s in sorted(python_words.items()):
    print(f"{w.title()} bu {s.lower()}dir!")
    """
"""
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}
print("Davlatlar nomlari:")
for davlat in sorted(davlatlar.keys()):
    print(f"{davlat.title()}")
print("Bu davlatlarning poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(f"{poytaxt.title()}")
davlat_1=input("Istalgan davlat nomini kiriting:")
poytaxt_1=davlatlar.get(davlat_1)
if davlat_1 in davlatlar:
    print(f"{davlat_1}ning poytaxti {poytaxt_1}dir!")
else:
    print("Bu davlat lug'atda mavjud emas!")
    """
"""
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
print("Yemoqchi bo'lgan taomingizni kiriting:")
taomlar=[]
for n in range(3):
    taomlar.append(input(f"{n+1}-taom nomini kiriting:").lower())
for taom in taomlar:
    if taom in menu:
        print(f"{str(taom.title())}ning narxi {menu[taom]}")
    else:
        print("Kechirasiz bizning menuda bunaqa taom mavjud emas!")
        """
"""
buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'asari':'sahih hadislar'
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent',
           'asari':'chinor'
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona",
           'asari':'madhiya'
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'asari':'Xamsa'
           }
mashhur_shaxslar=[buxoriy, qodiriy, vohidov, navoiy]
for mashhurlar in mashhur_shaxslar:
    print(f"{mashhurlar['ism']}ning asari {mashhurlar['asari']}dir!")
"""
"""
kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }
for dostim, kino in kinolar.items():
    print(f"{dostim.title()}ning sevimli kinolari: {kino}")
"""
"""
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
tanlov=input("Ma'lumot bilmoqchi bo'lgan davlatingiz nomini kiriting:").lower()
if tanlov in davlatlar:
    info=davlatlar[tanlov]
    if tanlov=="aqsh":
        print(f"{tanlov.upper()}: {info}")
    else:
        print(f"{tanlov.title()}: {info}")
else:
    print("Bu lug'atda bunday davlat mavjud emas!")
"""
"""
qiymatlar=[]
savol="Eng yoqtirgan kitoblaringiz nomini ayting"
savol+="(dasturni to'xtatish uchun 'stop' deb yozing):"
while True:
    qiymat=input(savol).lower()
    if qiymat!="stop":
        qiymatlar.append(qiymat.capitalize())
    else:
        break
print(f"Siz yoqtirgan kitoblar ro'yxati: {qiymatlar}dir!")
"""
"""
savol = "Muzeyga kirish narxini bilishni istasangiz yoshingizni kiriting"
savol += "(dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing):"
while True:
    qiymat=input(savol)
    if qiymat=="exit" or qiymat=="quit":
        break
    yosh=int(qiymat)
    if yosh<7:
        print("Siz uchun kirish narxi 2000 so'm")
    elif yosh<18:
        print("Siz uchun kirish narxi 3000 so'm")
    elif yosh<65:
        print("Siz uchun kirish narxi 10000 so'm")
    else:
        print("Sizga muzeyga kirish bepul!")
"""
"""
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat.title()=='Exit':
        break
    son=float(qiymat)
    if son<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
"""
"""
buyurtmalar=[]
savol="Iste'mol qilmoqchi bo'lgan tovarizni kiriting:"
ishora=True
while ishora:
    buyurtma = input(savol)
    buyurtmalar.append(buyurtma.title())
    savol2 =input("Dasturni to'xtatishni istasangiz 'stop' deb yozing!(yoki 'yo'q' deb yozing, ok mi?)")
    if savol2!="stop":
        continue
    else:
        ishora=False
print(f"Sizning buyurtmalaringiz:{buyurtmalar}")
"""
"""
mahsulotlar={}
while True:
    mahsulot=input("Menyuga qo'shmoqchi bo'lgan mahsulotingiz nomi nima?")
    narx=input(f"{mahsulot.title()}ning narxini kiriting:")
    mahsulotlar[mahsulot]=narx
    javob=input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob == "ha":
        continue
    else:
        break
print(mahsulotlar)
"""
"""
mahsulotlar={
    "osh":20000,
    "shashlik":17000,
    "sho'rva":15000,
    "grill":30000}
buyurtmalar=[]
while True:
    buyurtma=input("Iltimos, buyurtmangiz nomini kiriting:")
    buyurtmalar.append(buyurtma)
    if buyurtma in mahsulotlar.keys():
        print(f"{buyurtma}ning narxi: {mahsulotlar[buyurtma]} ga teng!")
    else:
        print("Bizda buyurtmangiz mavjud emas!")
    savol=input("Dasturni to'xtatishni istaysizmi?(ha/yo'q)")
    if savol!="ha":
        continue
    else:
        break
"""

def yosh_hisobla(ism,tugilgan_yil):
    """foydalanuvchi ismi va yoshini so'rab, necha yoshdaligini aniqlaydigan funksiya"""
    yosh=2023-tugilgan_yil
    print(f"{ism}, siz {yosh} yoshdasiz!")

def kvadrat_va_kub(son):
    """Son qabul qilib uning kvadrat va kublarini hisoblaydigan funksiya"""
    kvadrat=son**2
    kub=son**3
    print(f"{son}ning kvadrati {kvadrat} ga")
    print(f"Kubi esa {kub} ga teng!")

def juft_yoki_toq(son):
    """sonning juft yoki toq ekanligini aniqlaydigan funksiya"""
    qoldiq=son%2
    if qoldiq==0:
        print(f"{son} juft ekan!")
    else:
        print(f"{son} toq ekan!")
        
def qoldiqlarni_top(son):
    """Kiritilgan sonning 2 dan 10 gacha sonlarga qoldiqli bo'linishini tekshiruvchi funksiya"""
    bolinuvchilar=list(range(2,11))
    for bolinuvchi in bolinuvchilar:
        qoldiq=son%bolinuvchi
        if qoldiq!=0:
            print(f"{son}ning {bolinuvchi} ga bo'linganda qoldig'i {qoldiq}ga teng!")
        else:
            print(f"{son} {bolinuvchi} ga qoldiqsiz bo'linadi!")

def oraliq(min, max,qadam=1):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min +=qadam
    return sonlar
oraliq(0,23,3)
"""
def avtobiografiya(ism,familiya,otasining_ismi,t_yil,t_joy,email=None ,tel_number=None):
    malumotlar={
        "ismi":ism,
        "familiyasi":familiya,
        "otechestvo":otasining_ismi,
        "tugilgan_yil":t_yil,
        "tugilgan_joyi":t_joy,
        "elektron_manzil":email,
        "telefon_raqam": tel_number
        }
    return malumotlar
mijozlar=[]
while True:
    ism=input("Mijozning ismi:")
    familiya=input("Familiyasi:")
    otasining_ismi=input("Otasining ismini kiriting:")
    t_yil=int(input("Tug'ilgan yili"))
    t_joy=input("Tug'ilgan joyi")
    email=input("Elektron pochta(ixtiyoriy)")
    tel_number=input("Telefon raqam(ixtiyoriy)")
    savol=input("Yana bir mijoz qo'shasizmi?(ha/yo'q)")
    mijozlar.append(avtobiografiya(familiya,otasining_ismi ,t_yil,t_joy,email,tel_number))
    if savol=="ha":
       continue
    else:
        break
for mijoz in mijozlar:    
    print(f"Ismi:{ism};familiyasi:{familiya}; otasining ismi: {otasining_ismi}; tug'ilgan yili: {t_yil}; tug'ilgan joyi:{t_joy};elektron pochta:{email}; telefon raqami: {tel_number}")
"""
def katta_sonni_aniqla(x,y,z):
    """Kiritiladigan uchta sondan kattasini qaytaruvchi funksiya"""
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max
katta_sonni_aniqla(10,20,-5)

class Avto():
    def __init__(self, brend, model, rang, yil, korobka,probeg):
        self.brend = brend
        self.model = model
        self.rang = rang
        self.yil = yil
        self.korobka = "avtomat"
        self.probeg = 0
        
    def __repr__(self):
        return f"{self.brend} kompaniyasi, {self.rang} rangli {self.model} mashinasi"
        
    def get_brend(self):
        return self.brend
    
    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_yil(self):
        return self.yil
    
    def get_korobka(self):
        return self.korobka
    
    def get_probeg(self):
        return self.probeg
    
    def get_info_avto(self):
        return f"{self.brend} kompaniyasi, {self.model} rusumli, {self.rang} rangli, {self.yil} da chiqqan, {self.korobka} korobkali, {self.probeg} km yurigan mashina"
    
    def update_probeg(self, km):
        if km>0:
            masofa = self.probeg + km
        else:
            print("Iltimos musbat son kiriting")    
        return masofa


class AvtoSalon():
    
    def __init__(self,nom, manzil):
        self.nom = nom
        self.manzil = manzil
        self.sotuvdagi_avtolar = []
        
    def add_avto(self, avto):
        if isinstance(avto, Avto):
            self.sotuvdagi_avtolar.append(avto)
        else:
            print("Avto klassiga tegishli obyekt kiriting!")
        return self.sotuvdagi_avtolar
    
    def __repr__(self):
        return f"{self.nom} avtosaloni"
    
    def __getitem__(self, index):
        return self.sotuvdagi_avtolar[index]
    
    def __len__(self):
        return len(self.sotuvdagi_avtolar)
        

class Salon_manzili():
    
    def __init__(self, viloyat, tuman, mahalla, kocha, uy):
        self.viloyat = viloyat
        self.tuman = tuman
        self.mahalla = mahalla
        self.kocha = ""
        self.uy = uy
        
    def get_viloyat(self):
        return self.viloyat
    
    def get_tuman(self):
        return self.tuman
    
    def get_mahalla(self):
        return self.mahalla
    
    def get_kocha(self):
        return self.kocha
    
    def get_uy(self):
        return self.uy
    
    def get_manzil_info(self):
        return f"{self.viloyat.upper()} viloyati, {self.tuman.upper()} tumani, {self.mahalla.upper()} mahallasi, {self.kocha.upper()} ko'chasi, {self.uy} uyida joylashgan" 
        
        
salon_manzil = Salon_manzili("toshkent", "chilonzor", "botirma", "shuhrat","46-uy")


avto1 = Avto("Chevrolet", "Tracker", "qora", 2023, "avtomat", 24000)
avto2 = Avto("Chevrolet", "Lacetti", 'Qora', 2020, "Avtomat",95000)
avto3 = Avto("Chevrolet", "Malibu-2","Mokriy-asfalt",2023,"avtomat",15000)

avtosalon1 = AvtoSalon("Jaguar", salon_manzil)
for avto in [avto1, avto2, avto3]:
    avtosalon1.add_avto(avto)



        
    
    
    
        
    

   
            
    

    














