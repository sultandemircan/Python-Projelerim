#Kullanicidan alinan vize ve final notuna gore vizenin %40'ini ve finalin %60'ini alan ve sonucu ekranda gosteren ardindan ogrencinin kalip kalmadgini yazdiran kod
vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
print("Vize notu: ",vize, "Final notu: ",final)
ort = 0.4*vize + 0.6*final
print("Ortalamaniz: ",ort)
if (ort >= 50 ):
    print("Gectiniz")
elif (ort < 50):
    print("Kaldiniz")
else:
    print("Gecersiz deger girdiniz")
