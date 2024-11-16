import random
import time
print("""
************************
Sayı tahmin oyununa hoşgeldiniz...

1 ile 10 arasında bir sayı söyleyiniz.

5 hakkınız bulunmaktadır.

Çıkmak için '0' a basın.

************************
""")

rastgele_sayı = random.randint(1,10)
tahmin_hakkı = 5

while True:

    tahmin = int(input("tahmini sayınız:"))

    if (tahmin == 0):
        print("çıkış yapılıyor...")
        time.sleep(1)
        break

    if (tahmin < rastgele_sayı):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)
        print("daha yüksek sayı giriniz.")
        tahmin_hakkı -= 1

    elif (tahmin > rastgele_sayı):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)
        print("daha düşük bir sayı giriniz. ")
        tahmin_hakkı -= 1

    else:
        print("bilgiler sorgulanıyor...")
        time.sleep(1)
        print("tebrikler doğru bildiniz", "sayımız:", rastgele_sayı)
        break

    if (tahmin_hakkı == 0):
        print("tahmin hakkınız bitti.")
        print("sayımız:",rastgele_sayı)
        break






