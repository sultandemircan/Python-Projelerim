website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python  Programlama Rehberiniz (40 saat)"

# 1- " Hello World " ifadesindeki baş ve sondaki boşluk karakterlerini siliniz.
result = " Hello World ".strip()
result = " Hello World ".lstrip()
result = " Hello World ".rstrip()

result = website.lstrip("/:pth")

# 2- "www.sadikturan" ifadesindeki sadikturan bilgisi haricindeki her şeyi siliniz.
result = "www.sadikturan.com".strip("w.moc")


# 3- "course" dizisindeki tüm karakterleri küçük harf yapınız.
result = course.lower()
result = course.upper()
result = course.title()

# 4- "website" içinde kaç tane a karakteri vardır bulunuz.(count 'a')
result = website.count("a")
result = website.count("www")
result = website.count("www",0,10)

# 5- "website" www ile başlayıp com ile bitiyor mu?
result = website.startswith("www")
result = website.endswith("com")

# 6-"website" içinde '.com' ifadesi var mı?
result = website.find(".com")
result = website.find(".com",0,10)
result = course.find("Python")
result = course.rfind("Python")

result = website.index("com")
result = website.rindex("com")


# 7-"course" içindeki karakterlerin hepsi alfabetik mi?
result = course.isalpha()
result = "Hello".isalpha()
result = course.isdigit()
result = "123".isdigit()

# 8-"Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = "Contents".center(50)
result = "Contents".ljust(50, "*")
result = "Contents".rjust(50, "*")


# 9-"course" karakter dizisindeki tüm boşluk karakterlerini - ile değiştiriniz.
result = course.replace(" ", "-")
result = course.replace(" ", "-", 5)
result = course.replace(" ", "")

# 10-"Hello World" karakter dizisinin World ifadesini There olarak değiştiriniz.
result = "Hello World".replace("World", "There")

# 11-"course" karakter dizisini boşluk karakterlerinden  ayırınız.
message = course.split(" ")
 
print(result)