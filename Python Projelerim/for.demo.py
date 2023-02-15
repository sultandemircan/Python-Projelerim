sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır?
print("3'ün kati olan sayilar:")
for i in sayilar:
    if (i%3 == 0):        
        print(i)

# 2- Sayılar listesinde sayıların toplamı kaçtır ?
toplam = sum(sayilar)
print("Sayilar listesindeki sayilarin toplami = ",toplam)
toplam = 0
for i in sayilar:
    toplam += i
print("Sayilar listesindeki sayilarin toplami:", toplam)

# 3- Sayılar listesindeki tek sayıların karesini alınız.
for i in sayilar:
    if (i%2 != 1):
        print(i*i)

sehirler = ['Kocaeli', 'İstanbul', 'Ankara', 'İzmir', 'Rize']
# 4- Şehirlerden hangileri en fazla 5 karakterdir?
# for i in sehirler:
#     if (len(i)<=5):
#         print(i)


urunler = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'},
    
]
# 5- Ürünlerin fiyatları toplamı nedir?
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print('Toplam ürün fiyati: ',toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz

for urun in urunler:
    fiyat = int(urun['price'])
    if fiyat <= 5000:
        print(urun['name']) 
