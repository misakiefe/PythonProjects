toplam = 0
sayac = 0
while sayac < 10:
    sayi = float (input("Sayıyı girin: "))
    toplam += sayi
    sayac += 1
ortalama = toplam / 10
print("Girdiğiniz sayıların ortalaması : ", end="")
print(ortalama)