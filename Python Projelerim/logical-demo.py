# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input("Bir sayi giriniz: "))
result = (sayi>0 and sayi<100)
print(f"Girilen sayi 0-100 arasindami: {result}")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input("Bir sayi giriniz: "))
result = (sayi>0 and sayi%2==0)
print(f"Girdiğiniz sayi pozitif çift sayi mi: {result}")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = "sltndmrcn@gmail.com"
parola = "2558"
girilenEmail = input("Email adresinizi giriniz: ")
girilenParola = input("Parolanizi giriniz: ")
result = (girilenEmail=="sltndmrcn@gmail.com" and girilenParola== "2558")
print(f"Email adresiniz ve şifreniz doğrudur.{result}")

# 4- Girilen üç sayıyı  büyüklük olarak karşılaştırınız.
sayi1 = int(input("1.sayiyi giriniz: "))
sayi2 = int(input("2.sayiyi giriniz: "))
sayi3 = int(input("3.sayiyi giriniz: "))

result = (sayi1>sayi2) and (sayi1>sayi3)
print(f"1.sayi en büyük sayidir: {result}")

result = (sayi2>sayi1) and (sayi2>sayi3)
print(f"2.sayi en büyük sayidir: {result}")

result = (sayi3>sayi1) and (sayi3>sayi2)
print(f"3.sayi en büyük sayidir: {result}")


# 5- Kullanıcıdan iki vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = float(input("Birinci vize notunuzu giriniz: "))
vize2 = float(input("İkinci vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ort = ((vize1+vize2)/2)*0.6 + (final*0.4)
result = (ort>50 and final>=50) or (final>=50)
result = (ort>50) or (final>=70)
print(f"Öğrencinin ortalamasi: {ort} ve geçme durumu: {result} ")


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
result1 = zayif = (index>0) and (index<=18.4)
print(f"Zayif grubundasiniz.{result1}")
result2 = normal = (index>=18.5) and (index<=24.9)
print(f"Normal grubundasiniz.{result2}")
result3 = kilolu = (index>=25) and (index<=29.9)
print(f"Kilolu grubundasiniz.{result3}")
result4 = şişman = (index>=30) and (index<=34.9)
print(f"Şişman grubundasiniz.{result4}")




