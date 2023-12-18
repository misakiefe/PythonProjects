"""
Rüzgar hangi açıyla esiyor
Değerine göre aralıklar kontrol edilerek hangi yönden estiği yazılıcak
"""
deger = int(input("Rüzgarın hangi açıyla estiğini yazınız (0-360) = "))
if deger >= 0 and deger <= 20:
    print("Yıldız Poyraz!")
elif deger >= 20 and deger <= 40:
    print("Poyraz!")
elif deger >= 40 and deger <= 60:
    print("Gündoğuşu Poyraz!")
elif deger >= 60 and deger <= 80:
    print("Gün Doğuşu!")
elif deger >= 80 and deger <= 100:
    print("Gündoğuşu Keşişleme!")
elif deger >= 100 and deger <= 120:
    print("Keşişleme")
elif deger >= 120 and deger <= 140:
    print("Kıble Keşişleme")
elif deger >= 140 and deger <= 160:
    print("Kıble")
elif deger >= 160 and deger <= 180:
    print("Kıble Lodosu")
elif deger >= 180 and deger <= 200:
    print("Lodos")
elif deger >= 200 and deger <= 220:
    print("Batı Lodos")
elif deger >= 220 and deger <= 240:
    print("Batı")
elif deger >= 240 and deger <= 260:
    print("Batı Karayel")
elif deger >= 260 and deger <= 280:
    print("Karayel")
elif deger >= 280 and deger <= 300:
    print("Yıldız Karayel")
elif deger >= 300 and deger <= 360:
    print("Yıldız")
else:
    print("Geçersiz değer.")