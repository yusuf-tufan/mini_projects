print("""--------------------------------
1.harf ayırır.

2.harfleri alt alta yazdırır.

3.harf arasına "/" işareti koyar.

4.harf arasına "*"işareti koyar.
---------------------------------""")

a = input("cümlenizi giriniz:")

işlem = input("Hangi işlemi yapmak istersiniz:")

if (işlem== "1"):
    print(*a,sep="\t")
elif (işlem=="2"):
    print(*a,sep="\n")
elif (işlem=="3"):
    print(*a,sep="/")
elif (işlem=="4"):
    print(*a,sep="*")
else :
    print("Geçersiz işlem...")
