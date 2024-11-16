print("""
***********************************

1.toplama işlemi
2.çıkarma işlemi
3.çarpma işlemi
4.bölme işlemi
5.üs alma işlemi
6.ekok işlemi
7.ebob işlemi
8.logaritma işlemi
9.kareköklü sayılar işlemi
10.kosinüs teoremi işlemi
11.sinüs teoremi işlemi

ÇIKIŞ için 'q' ya basınız.
***********************************
""")

import math
import time

while True:
    işlem = input("işlem seçiniz:")
    if (işlem == "q"):
        print("çıkış yapılıyor...")
        time.sleep(1)
        break

    elif (işlem == "1"):
        print("toplama işlemi seçildi.")
        x=int(input("1. sayınız:"))
        y=int(input("2. sayınız:"))
        print("işlemin sonucu =",x+y)

    elif (işlem == "2"):
        print("çıkarma  işlemi seçildi.")
        x = int(input("1.sayınız:"))
        y = int(input("2.sayınız:"))
        print("işlemin sonucu =",x-y)

    elif (işlem == "3"):
        print("çarpma işlemi seçildi.")
        x = int(input("1.sayınız:"))
        y = int(input("2.sayınız:"))
        print("işlemin sonucu =", x*y)

    elif (işlem == "4"):
        print("bölme işlemi seçildi.")
        x = int(input("1.sayınız:"))
        y = int(input("2.sayınız:"))
        print("işlemin sonucu =", x / y)

    elif (işlem == "5"):
        print("üs alma işlemi seçildi.")
        x=int(input("sayınız:"))
        y=int(input("derecesini giriniz:"))
        print("işlem sonucu:",x**y)

    elif (işlem == "6"):
        print("ekok işlemi seçildi.")
        x = int(input("1.Sayınız:"))
        y = int(input("2.Sayınız:"))

        def ekok_fonk(x, y):
            kat = 1
            while True:
                ekok = x * kat
                kat += 1
                if ekok % y == 0:
                    return ekok
        print("Sonuc= {}".format(ekok_fonk(x, y)))

    elif (işlem == "7"):
        print("ebob işlemi seçildi.")
        x = int(input("1.sayınız:"))
        y = int(input("2.sayınız:"))

        def ebob(x,y):
            i=1
            ebob=1
            while ( i<= x and i<=y):
                if not (x % i) and not ( y % i):
                    ebob = i
                i +=1
            return ebob
        print("işlemin sonucu:",ebob(x,y))

    elif (işlem == "8"):
        print("logaritma işlemi seçildi.")
        x = int(input("iç sayıyı giriniz:"))
        y= int(input("taban sayı giriniz:"))
        print("log{}({}):".format (y,x),math.log(x,y ))

    elif (işlem == "9"):
        print("karekök işlemi seçildi.")
        x = int(input("kökü hesplanılacak sayı:"))
        print("işlem sonucu:",math.sqrt(x))

    elif (işlem == "10"):
        print("kosinüs işlemi seçildi.")
        x = int(input("Açı giriniz:"))
        x=x*math.pi/180
        print("işlem sonucu:",math.cos(x))

    elif (işlem == "11"):
        print("sinüs işlemi seçildi.")
        x = int(input("Açı giriniz:"))
        x = x * math.pi/180
        print("işlem sonucu:",math.sin(x))

    else:
        print("lütfen doğru işlem sayısı giriniz!")
        continue








