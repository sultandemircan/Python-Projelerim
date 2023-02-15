# "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
cars = ["BMW", "Mercedes", "Opel", "Mazda"]

# Liste kaç elemanlıdır
result = len(cars)

# Listenin ilk ve son elemanı nedir
#result = (cars[0])
#result = (cars[3])

# Mazda değerini Toyota ile değiştirin
cars[3] = "Toyota"
result = cars


# Mercedes listenin bir elemanı mıdır?
result = "Mercedes" in cars

# Listenin -2 indexindeki değer nedir 
result = cars[-2]

# Listenin ilk 3 elemanını alın.
result = cars[0:3]

#Listenin son iki elemanı yerine "Toyota" ve "Renault" u ekleyin
cars[-2:] = ["Toyota", "Renault"]
result = cars

# Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
result = cars + ["Audi", "Nissan"] 


# Listenin son elemanını silin
del cars[-1]
result = cars

# Listenin elemanlarını tersten yazdırınız.
result = cars[::-1]


# Aşağıdaki verileri bir liste içinde saklayınız
     # student A: Yiğit Bilgi 2010,  (70, 60, 70)
     # student B: Sena Turan 1999,   (80, 80, 70)
     # student C: Ahmet Turan 1998,  (80, 70, 90)

studentA = ["Yiğit", "Bilgi", 2010, [70, 60, 70]]
studentB = ["Sena", "Turan", 1999, [80, 80, 70]]
studentC = ["Ahmet", "Turan", 1998, [80, 70, 90]]

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2022-studentA[2]} yaşındadır ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3} dır"


print(result)