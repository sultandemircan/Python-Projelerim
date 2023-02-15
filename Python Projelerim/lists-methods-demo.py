names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1- "Cenk ismini listenin sonuna ekleyiniz."
names.append("Cenk")
print(names)

# 2- " Sena değerini listenin başına ekleyiniz."
names.insert(0,"Sena")
print(names)

# 3- "Deniz ismini listeden siliniz."
names.pop(4)
names.remove('Deniz')
print(names)

# 4- "Deniz isminin indeksi nedir ?"
result = names.index("Deniz")

# 5- "Ali" listenin bir elemanı mıdır ?   result
result = "Ali" in names
result = names.index('Ali')

# 6- Liste elemanlarını ters çeviriniz.
names.reverse()
print(names)

# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.  
years.sort()
print(years)

# 9- str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.      
str = "Chevrolet , Dacia"
result = str.split(',')

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
result = max(years)
result = min(years)

# 11- years dizisinde kaç tane 1998 değeri vardır ?          
result = years.count(1998)

# 12- years dizisinin tüm elemanlarını siliniz.
result = years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []


marka = input("3 adet araç markasi giriniz: ")
markalar.append()

marka = input("3 adet araç markasi giriniz: ")
markalar.append()

marka = input("3 adet araç markasi giriniz: ")
markalar.append()


print(markalar)




print(result)