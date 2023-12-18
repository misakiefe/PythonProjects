"""konsoldan hava sıcaklığı alınacak
hava sıcaklığı 0 altındaysa dondurucu
0 - 10 arasındaysa soğuk
10 - 18 arasındaysa ılık
18 - 30 arasındaysa sıcak
30+ üstündeyse cok sıcak"""
havasicaklik = int(input("Hava sıcaklığını giriniz = "))
if havasicaklik < 0:
    print("Dondurucu!")
elif havasicaklik >= 10 and havasicaklik <= 18:
    print("Ilık!")
elif havasicaklik >= 18 and havasicaklik <= 30:
    print("Sıcak!")
elif havasicaklik > 30:
    print("Çok Sıcak!")
else:
    print("Lütfen hava sıcaklığını girin.")
