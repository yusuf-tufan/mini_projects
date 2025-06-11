print("""-------------------------------------
1.İşlem toplama işlemi

2.İşlem çıkarma işlemi

3.İşlem çarpma işlemi

4.İşlem bölme işlemi
-------------------------------------
""")
a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))

işlem = input("İşlem giriniz:")

if işlem == "1":
    print("{} + {} = {}".format(a,b,a+b))
elif işlem == "2":
    print("{} - {} = {}".format(a,b,a-b))
elif işlem == "3":
    print("{} * {} = {}".format(a,b,a*b))
elif işlem == "4":
    print("{} / {}  = {}".format(a,b,a/b))
else :
    print("Geçersiz işlem...")
