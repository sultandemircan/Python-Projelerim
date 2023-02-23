#Kullanicidan aldigimiz boy ve kiloyu vucut kitle indeksi hesaplama formulu uygulayarak kullanicinin vucut kitle indeksini hesaplayan kod
#Vucut kitle indeksi hesaplama = kilo / (boy*boy)

kilo = input("Kilonuzu giriniz :")
kilo = float(kilo)
boy = input("Boyunuzu metre cinsinden giriniz: ")
boy = float(boy)
print("Girilen boy :",boy, "Girilen kilo :",kilo)


indeks = (kilo / (boy*boy))
indeks = float(indeks)
print("Vucut kitle indeksiniz: " , indeks)
if indeks < 18:
    print("Zayif")
elif indeks >= 18 and indeks < 25:
    print("Normal")
elif indeks >=25 and indeks < 30:
    print("Kilolu")
elif indeks >=30 and indeks < 35:
    print("Obezite")
else:
    print("Ciddi Obezite")





