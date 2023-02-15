# 1- Girilen iki sayıdan hangisi büyüktür?
sayi1 = int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("İkinci sayiyi giriniz: "))
result = sayi1 > sayi2
print(f"sayi1: {sayi1} sayi2: {sayi2} den büyüktür. {result}")

# 2- Kullanıcıdan iki vize (%60) ve final (%40) alıp ortalamasını hesaplayınız.
# Eğer ortalama 50'nin altındaysa kaldı yazdırın.
vize1 = float(input("Birinci vize notunuzu giriniz: "))
vize2 = float(input("İkinci vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ort = (((vize1+vize2)/2) * 0.6 ) + (final * 0.4)
print(f"Not ortalamaniz: {ort} ve dersten geçme durumunuz: {ort>=50} ")


# 3- Girilen bir sayını  tek mi çift mi olduğunu yazdırınız.
sayi = int(input("Bir sayi giriniz: "))
tekcift = (sayi % 2 == 0)
print(f"Girilen sayinin çift olma durumu: {tekcift}")

# 4- Girilen  bir sayının negatif pozitif durumunu yazdırınız.
sayi = int(input("sayi: "))
pozitifmi = (sayi > 0)
print(f"Girilen sayinin pozitif olma durumu : {pozitifmi}")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
# (email: email@sadikturan.com   parola: abc123)

email = "email@sadikturan.com"
parola = "abc123" 

girilenEmail = input("email adresinizi giriniz: ")
girilenParola = input("Parolanizi giriniz: ")

isEmail = (email == girilenEmail)
isParola = (parola == girilenParola )
print(f"Email bilgi doğru mu: {isEmail} ve Parola doğru mu {isParola}")