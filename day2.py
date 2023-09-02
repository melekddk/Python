faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)

#print(int(krediAdi)) 
faiz= str(faiz)
print(type(faiz))

# Kullanıcıdan alınan değerler default olarak string yapıdadır.
vade = int(input("Lütfen istediğiniz vade sayısını giriniz : "))
print(type(vade))

print(vade + 12)

vade = vade + 12

#string interpolation yöntemi
#Seçtiğiniz vade sonucu ortaya çıkan vade : 
# ALT + Z ile ekrana sığmayan komutları alt alta alıyor.
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))

print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi = vade))

print(f"Seçtiğiniz vade sonucu ortaya çıkan vade : {vade}")

isim = input("Lütfen isminizi giriniz : ")
metin = "Merhaba {name}".format(name = isim)

print(metin)

# f-string yöntemi

metin = f"Hoşgeldiniz {isim}"
print(metin)


#listeler
#döngüler
#fonksiyonlar