import sys
import datetime
def derecedonustur():
    derecebicimi = input("""Derece çeşidinizi giriniz.
    C = Selsiyus F = Fahrenheit : """)
    sicaklik = float(input("Sıcaklığınızı giriniz : "))
    if derecebicimi == "C":
        print("Sizin fahrenheit sıcaklık değeriniz: ", end="")
        print(sicaklik * 9 / 5 + 32)
    if derecebicimi == "F":
        print("Sizin selsiyus sıcaklık değeriniz: ", end="")
        print(sicaklik - 32 * 5 / 9)
def hesapmakine():
    print("Lütfen Integer mı Float mı işlem yapmak istersiniz: ")
    print("Integer: 1")
    print("Float: 2")
    secim = input("Seçiminizi Yapın : (1 veya 2) : ")
    if secim == "1":
        print("Ondalık sayı girmeyin!")
        sayi1 = int(input("İlk sayıyı girin: "))
        sayi2 = int(input("İkinci sayıyı girin: "))
        islem = input("""Yapmak istediğiniz işlemi giriniz
        (Toplama = +, Çıkarma = -, Çarpma = *, Bölme = /)
        """)

        if islem == "+":
            print("Hesap makinesi sizin için hesapladı. Sonuç: " + str(sayi1 + sayi2))

        elif islem == "-":
            print("Hesap makinesi sizin için hesapladı. Sonuç: " + str(sayi1 - sayi2))

        elif islem == "*":
            print("Hesap makinesi sizin için hesapladı. Sonuç: " + str(sayi1 * sayi2))

        elif islem == "/":
            print("Hesap makinesi sizin için hesapladı. Sonuç: " + str(sayi1 / sayi2))
    elif secim == "2":
        sayi1 = float(input("İlk sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        islem = input("""Yapmak istediğiniz işlemi giriniz
        (Toplama = +, Çıkarma = -, Çarpma = *, Bölme = /)
        """)

        if islem == "+":
            print("Hesap makinesi sizin için hesapladı. Sonuç: " + str(sayi1 + sayi2))

        elif islem == "-":
            print("Hesap makinesi sizin için hesapladı. Sonuç: " + str(sayi1 - sayi2))

        elif islem == "*":
            print("Hesap makinesi sizin için hesapladı. Sonuç: " + str(sayi1 * sayi2))

        elif islem == "/":
            print("Hesap makinesi sizin için hesapladı. Sonuç: " + str(sayi1 / sayi2))
    else:
        print("Geçersiz seçenek. Lütfen 1 veya 2 girin.")
def robotyap():
    import sys

    print("İnsanoğlu için faydalı bir robot yapın!")

    zeka = int(input("Robotunuzun Zeka Seviyesi (1-10) : "))
    guc = int(input("Robotunuzun Güç Seviyesi (1-10) : "))
    boy = int(input("Robotunuzun Boyu (150-200cm) : "))
    gorunus = int(
        input("Robotunuzun Nasıl Görüneceğini Yazın. (1: çok insansı, 2: normal robot 3:Kablolardan oluşuyor.) : "))

    if gorunus not in [1, 2, 3]:
        print("Geçersiz görünüş seçimi. Lütfen 1, 2 veya 3 girin.")
        sys.exit()

    if zeka not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print("Geçersiz zeka seçimi Lütfen 1 ve 10 arasında bir rakam girin.")
        sys.exit()

    if guc not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print("Geçersiz güç seçimi Lütfen 1 ve 10 arasında bir rakam girin.")
        sys.exit()
    if boy not in [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 167, 168, 169, 170,
                   171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 181, 182, 183, 184, 185, 186, 187, 188, 189,
                   190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]:
        print("Lütfen 150 200 Arasında sayı girin ")
        sys.exit()
    if zeka >= 8:
        print("Robotunuz çok zekalı olduğu için İnsanoğlu için bir Felaket oldu.")
        sys.exit()
    if zeka <= 4:
        print("Robotunuz zekası çok düşük olduğu için İnsanoğlu için bir Felaket oldu. ")
        sys.exit()
    if guc and zeka >= 8:
        print(
            "Robotunuz çok güçlü ve zekalı olduğu için insanlardan daha iyi düşünmeye başladı ve İnsanoğlu için bir Felaket oldu.")
        sys.exit()
    if gorunus >= 3:
        print("Robotunuz kablolardan olup ve dış görünüşü olmadığı için İnsanoğlu için bir Felaket oldu.")
        sys.exit()
    elif gorunus == 1:
        print("Robotunuz çok insansı olduğu için İnsanoğlu için bir Felaket oldu.")
        sys.exit()
    if guc >= 8:
        print("Robotunuz çok güçlü olduğu için İnsanoğlu için bir Felaket oldu")
        sys.exit()
    if guc <= 4:
        print("Robotunuz çok güçsüz olduğu için İnsanoğlu için bir Felaket oldu")
        sys.exit()

    else:
        basarili = print("Robutunuz insaoğlu için çok yararlı oldu")
    isim = input("İsminizi Öğrenebilirmiyim? : ")

    print(f"Tebrikler {isim} ")
def karekokhesapla():
    import math
    sayi = int(input("Sayınızı Girin : "))
    print("Hesaplandı!", end=" ")
    print(math.sqrt(sayi))
def dogumyilhesaplama():
    import sys
    def hesaplama():
        dogumyil = int(input("Doğum yılınızı giriniz : "))
        yil = 2023
        yas = yil - dogumyil
        print("Yaşınız hesaplandı!: ", end="")
        print(yas)

    evethayir = input("""Yaşınızı Hesaplatmak istiyor musunuz?
    1 = Evet.
    2 = Hayır.
     = """)
    if evethayir == "1":
        hesaplama()
    elif evethayir == "2":
        print("Görüşmek üzere.")
        sys.exit()
    else:
        print("Sayı gir.")
def taskagitmakas():
    import random

    def kazanan_belirle(oyuncu, bilgisayar):
        if oyuncu == bilgisayar:
            return "Berabere!"
        elif (oyuncu == "taş" and bilgisayar == "makas") or \
                (oyuncu == "kağıt" and bilgisayar == "taş") or \
                (oyuncu == "makas" and bilgisayar == "kağıt"):
            return "Kazandın!"
        else:
            return "Kaybettin!"

    def main():
        while True:
            print("\nTaş, Kağıt, Makas oyununa hoş geldiniz!")
            print("Seçenekler: taş, kağıt, makas, çıkış")

            oyuncu_secim = input("Lütfen seçiminizi yapın: ").lower()

            if oyuncu_secim == "çıkış":
                print("Oyunu kapatılıyor...")
                break
            elif oyuncu_secim not in ["taş", "kağıt", "makas"]:
                print("Geçersiz bir seçim. Lütfen tekrar deneyin.")
                continue

            bilgisayar_secim = random.choice(["taş", "kağıt", "makas"])

            print(f"Bilgisayarın seçimi: {bilgisayar_secim}")

            sonuc = kazanan_belirle(oyuncu_secim, bilgisayar_secim)
            print(f"Sonuç: {sonuc}")

    if __name__ == "__main__":
        main()
#########################################################
saatsuan = datetime.datetime.now()
print(f"""Multiasking Client programına hoşgeldiniz.
   Bu program'da dilediğiniz şeyleri yaptırabilirsiniz
   Şuan saat : {saatsuan.hour}:{saatsuan.minute}
   1 - Derece Dönüştürme.
   2 - Hesap Makinesi
   3 - Robot Yapma Oyunu
   4 - Karekök Hesaplama
   5 - Yaş Hesaplama oyunu.
   6 - Taş Kağıt Makas oyunu.
   7 - Çıkış""")
gsayi = input("Bir sayı girin. 1 - 7 rasında : ")
if gsayi == "1":
    derecedonustur()
elif gsayi == "2":
    hesapmakine()
elif gsayi == "3":
    robotyap()
elif gsayi == "4":
    karekokhesapla()
elif gsayi == "5":
    dogumyilhesaplama()
elif gsayi == "6":
    taskagitmakas()
elif gsayi == "7":
    print("Görüşmek üzere.")
    sys.exit()
else:
    print("Lütfen 1 - 7 Arasında sayı girin. ")









