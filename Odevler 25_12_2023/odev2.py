toplam = 0
sayac = 0
while True:
        sayi = float(input("Bir sayı girin (döngünden çıkmak için 0): "))
        if sayi == 0:
            break
        toplam += sayi
        sayac += 1
if sayac > 0:
    ortalama = toplam / sayac
    print("girdiğiniz sayıların ortalaması ", end="")
    print(ortalama)
else:
    print("sayı girmelisin!")
