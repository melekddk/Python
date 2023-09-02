print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)

#string=> metinsel ifade.
# yorum satırları
#terminalde kodu çalıştırmak için python  dosya adı olacak (python main.py)

baslik = "İhtiyaç Kredisi"

print(baslik)

#integer, int = tam sayı
vade = 36
ekVade = 6
vade2 = "36"

#float, decimal, double
aylikOdeme =200.50

#bool, boolean => True, false
yukselisteMi = True

#matematiksel operatörler

print(5 + 5)

print(vade + 12)
print(vade + ekVade)

print(5-5)
print(vade - 13)
print(vade - ekVade)

# *

print( 8*10)
print(vade * ekVade)

# /
print(80/2)
print(vade / ekVade)

yeniVade = vade / 2
fiyat =100
indirimliFiyat = fiyat -20

print(yeniVade)
print(indirimliFiyat)


# %= mod operatörü

print(10%2)

print(vade % 5)
print(30 % 10)

# mantıksal operatörler ya da karşılaştırma operatörleri

print(1 == 1)
print(1 == 2)

# CTRL K + CTRL C
# CTRL + Ö  yorum satırını çoklu alıp aynı şekilde çıkarıyor
print(1>2)
print(3>1)
print(1>1)
print(1>=1)

print(1<2)
print(3<1)
print(1<1)
print(1<=1)

print(1 != 2 )
print(1 != 1)

# or = veya and = ve 


print(1 > 2 or 5 > 2)

print(1 > 2 and 5 > 2)

print(1 > 2 or 5 > 2 and 3 >2)

print(1 > 2 and 5 > 2 and 3 > 2)

print( 2 > 1 or 1 > 2 and 3 > 2)



#karar yapıları
# if else - elif
sayi1 =50
sayi2 = 50 

# sayi1 sayi2 den büyükse ekrana sayi 1 daha büyük yazdir

if sayi1 < sayi2:
    print("Sayı 1 Sayı 2'den küçüktür")
    print("Hala if bloğunun içerisindeyim")
elif sayi1==sayi2:
    print("İki sayı eşittir")

#eğer if bloguna girmez ise
else:
    print("Sayı 1 Sayı 2'den büyüktür")

    
print("Bu if bloğunun dışıdır")








