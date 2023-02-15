#Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız.
pi=3.14
r = float(input("Yariçap değerini giriniz: "))
print("Yariçap değeri=",r)
cevre=2*pi*r
print(type(cevre))
alan=pi*r*r
print(type(alan))
print("Dairenin çevresi = ",cevre)
print("Dairenin alani = ",alan)
