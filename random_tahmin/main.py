import time
import random

print("SAYI TAHMIN OYUNU")

rastgele_sayi = random.randint(1,50)
tahmin_hakki=7
while True:
    tahmin = int(input("tahmininiz: "))

    if(tahmin<rastgele_sayi):
        print("bilgileriniz sorgulaniyor")
        time.sleep(1)
        print("daha yuksek bir sayi soyleyin ")
        tahmin_hakki-=1
    elif(tahmin>rastgele_sayi):
        print("bilgileriniz sorgulaniyor")
        time.sleep(1)
        print("daha dusuk bir sayi soyleyin ")
        tahmin_hakki-=1
    else:
        print("bilgileriniz sorgulaniyor")
        time.sleep(1)
        print("tebrikler sayiyi bildiniz",rastgele_sayi)
        break
    if(tahmin_hakki ==0 ):
        print("tahmin hakkiniz bitti")

