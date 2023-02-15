sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesini while ile ekrana yazdırın.
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayilari ekrana yazdirin.
baslangic = int(input("Lütfen bir başlangiç değeri giriniz: "))
bitis = int(input("Lütfen bir bitiş değeri giriniz: "))

i = baslangic
while i < bitis:
    i += 1
    if(i%2 == 1):
        print(i)
       
    
# 3- 1-100 arasindaki sayilari azalan şekilde yazdirin.
x = 100
while (x >= 1):
    print(x)
    x -= 1


# 4- Kullanicidan alacağiniz 5 sayiyi ekranda sirali bir şekilde yazdiriniz.
numbers = []
i = 0

while i<5:
    sayi = int(input('Sayi:'))
    numbers.append(sayi)
    i += 1
numbers.sort()
print(numbers)
 

# 5- Kullanicidan alacağiniz sınırsız ürün bilgisini ürünler listesi içinde saklayiniz.
# ** Ürün sayısını kullanıcıya sorun.
# ** Dictionary listesi yapısı (name,price) şeklinde olsun.
# ** Ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
 
urunler = []
adet = int(input("Kaç adet ürün eklemek istiyorsunuz: "))
i = 0

while(i<adet):
    name = input("Ürün ismi: ")
    price = input("Ürün fiyati: ")
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f"Ürünün ismi: {urun['name']} ürünün fiyati:{urun['price']}")