# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme dueumunu kontrol ediniz.
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
isim = input(" İsminizi ve soyisminizi giriniz:")
yas = int(input("Yaşinizi giriniz:"))
egitimdurumu = input("Eğitim durumunuzu giriniz: ")

if (yas >= 18): 
    if (egitimdurumu == "Lise " or egitimdurumu == "Üniversite"):
        print("Ehliyet alabilirsiniz")
    else:
        print(f"{isim} Ehliyet alamazsiniz eğitim durumunuz tutmuyor")
else:
    print(f"{isim} Ehliyet alamazsiniz yaşiniz tutmuyor")


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
# 0 - 24 => 0
# 25 - 44 => 1
# 45 - 54 => 2
# 55 - 69 => 3
# 70 - 84 => 4
# 85 - 100 => 5
yazili1 = int(input("1.Yazili notunuzu giriniz:"))
yazili2 = int(input("2. yazili  notunuzu giriniz:"))
sözlü = int(input("Sözlü notunuzu giriniz: "))
ort = (yazili1 + yazili2 +sözlü)/3
if (ort>0 and ort<25):
    print("Notunuz 0 dir")
elif (ort>=25 and ort<=44):
    print("Notunuz 1 dir.")
elif (ort>=45 and ort<=54):
    print("Notunuz 2 dir.")
elif (ort>=55 and ort<=69):
    print("Notunuz 3 tür.")
elif (ort>=70 and ort<=84):
    print("Notunuz 4 tür.")
else:
    print("Notunuz 5 tir.")


# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
# 1.Bakım => 1.yıl
# 2.Bakım => 2.yıl
# 3.Bakım => 3.yıl
# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
# *** Datetime modülünü kullanmanız gerekiyor.
# (simdi) - (2018/8/1)

import datetime

tarih = int(input("Araciniz hangi tarihte trafiğe çikti gün/ay/yil: "))
tarih = tarih.split('/')
# print(tarih[0])
# print(tarih[1])
# print(tarih[2])
trafigeCikis = datetime.datetime(tarih[0], tarih[1], tarih[2])
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
    print("1.servis araliği")
elif days>365 and days<=365*2:
    print("2.servis araliği")
elif days>365*2 and days<=365*3:
    print("3.servis araliği")
else:
    print("Hatali süre girdiniz")