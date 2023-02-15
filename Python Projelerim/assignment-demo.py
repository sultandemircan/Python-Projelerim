x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız iki sayının çarpımı ile x,y,z toplamının farkı nedir?
sayi1 = int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("İkinci sayiyi giriniz: "))
carpim = sayi1 * sayi2
print("Çarpim sonucu: " , carpim)
toplam = x+y+z
print("x, y, z toplam sonucu: ", toplam)
fark = toplam - carpim 
print("Fark: ", fark)


# 2- y'nin x'e kalansız bölümünü hesaplayınız.
bolum = y // x 
print(bolum)

# 3- (x,y,z) toplamının mod 3'ü nedir?
toplam = x+y+z
mod = toplam % 3
print(mod)

# 4- y'nin x. kuvveti nedir?
sonuc = y **x
print(sonuc)

# 5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır?
x, *y, z = numbers
print(x, y, z)
kup = z*z*z      
print("z'nin küpü: ", kup)

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır?
x, *y, z = numbers
print(y)
toplam = y[0] + y[1] + y[2]
print("y'nin değerleri toplami: ", toplam)