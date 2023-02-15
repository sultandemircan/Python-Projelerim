# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input("Bir sayi giriniz:"))
if (sayi>=0 and sayi<=100):
    print("Girdiğiniz sayi 0 - 100 arasindadir.")
else:
    print("Girdiğiniz sayi 0 - 100 arasinda değildir")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input("Bir sayi giriniz: "))
if sayi>0:
    if (sayi%2 == 0):
     print("Girdiğiniz sayi pozitif çift sayidir.")
    else:
     print("Girdiğiniz sayi pozitif fakat tek sayidir.")
else:
     print("Girdiğiniz sayi  negatiftir")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = "sltndmrcn@gmail.com"
parola = "2558"
girilenEmail = input("email adresinizi giriniz: ")
girilenPassword = input("Şifrenizi giriniz:")
if(email == girilenEmail):
     if(parola == girilenPassword):
         print("email adresiniz ve parolaniz doğrudur.")
     else :
         print("email adresiniz doğru fakat parolaniz yanliştir")
else:
     print("email adresiniz hatalidir.")



# 4- Girilen üç sayıyı  büyüklük olarak karşılaştırınız.
sayi1 = int(input("1.sayiyi giriniz: "))
sayi2 = int(input("2.sayiyi giriniz: "))
sayi3 = int(input("3.sayiyi giriniz: "))
if(sayi1> sayi2 and sayi1>sayi3):
     print("1.sayi en büyüktür.")
elif(sayi2>sayi1 and sayi2>sayi3):
     print("2.sayi en büyüktür.")
else:
     print("3.sayi en büyüktür.")



# 5- Kullanıcıdan iki vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input("Birinci vize notunuzu giriniz: "))
vize2 = float(input("İkinci vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ort = ((vize1+vize2)/2)*0.6 + (final*0.4)
print("Ortalamaniz = ", ort)
if (ort>=50 and final == 50):
     print("Geçtiniz")
elif(ort>=50 and final <=70):
     print("Geçtiniz11111")
else:
     print("Kaldiniz")
  

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül = (Kilo/boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4     => Zayıf
#    18.5-24.9  => Normal
#    25.0-29.9  => Fazla Kilolu
#    30.0-34.9  => Şişman(Obez)

input("İsminizi giriniz: ")
kilo = float(input("Kilonuzu giriniz: "))
boy = float(input("Boyunuzu metre cinsinden giriniz: "))
index = (kilo/(boy*boy))
print("Vücut Kitle indexiniz: ",index)
if(index>=0 and index<=18.4):
    print("Zayif grubundasiniz")
elif(index>=18.5 and index<=24.9):
    print("Normal grubundasiniz")
elif(index>=25.0 and index<=29.9):
    print("Fazla kilolu grunudasiniz")
elif(index>=30.0 and index<= 34.9):
    print("Şişman grubundasiniz")
else:
    print("Hatali değer girdiniz")

