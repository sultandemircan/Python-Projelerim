website = "http://www.sadikturan.com"
course = "Python Kursu:Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- course karakter dizisinde kaç karakter bulunmaktadır?
result = len(course)     #hocanın çözümü
length=len(website)
print(len(course))       #benim çözümüm

# 2- website içinden www karakterlerini alın 
result = website[7:10]              #hocanın çözümü
print(website[7:10])                #benim çözümüm

# 3- website içinden com karakterleni alın
result=website[22:25]                #hocanın çözümü
result=(website[length-3:length])
print(website[22:25])                #benim çözümüm

# 4- course içinden ilk 15 ve son 15 karakteri alın
print(course[0:16])
print(course[-15:])

# 5- course ifadesindeki karakterleri tersten yazdırın 
result = course[: :-1]
print(result)

name, surname, age, job = "Bora", "Yilmaz", "32", "Mühendislik"
# 6- Yukarıda verilen değişkenlerle aşağıdaki ifadeleri yazdırınız.
# Benim adım Bora Yılmaz yaşım 32 ve mesleğim mühendislik.
result="Benim adim {0} {1} yaşim {2} ve mesleğim {3}".format(name, surname, age, job)
result=f"Benim adim {name} {surname} yaşim {age} ve  mesleğim {job}."
print(result)

# 7-Hello world ifadesindeki w'yi W ile değiştirin 
s="Hello world"
s= s[0:6] + "W" + s[-4:]
print(s)
#s.replace("w","W")


# 8- "abc" ifadesini yan yana 3 defa yazdırın

result="abc " *3
print(result)