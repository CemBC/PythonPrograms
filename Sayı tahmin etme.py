import random
import time

print("""""

        SAYI TAHMİN ETME OYUNU
      
      1 ile 40 arasında rastgele bir sayıyı
            tahmin ediniz.
            Tahmin hakkınız = 7
            
""""")
sayı = random.randint(1,40)
hak = 7
while True:
    a =int(input("Sayı tahmininiz:"))
    if a > sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tahmininiz bulunması gereken sayıdan büyük.")
        hak -= 1
    elif a < sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tahmininiz bulunması gerekn sayıdan küçük.")
        hak -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler sayıyı buldunuz!")
        break
    if hak== 0:
        print("Tahmin hakkınız bitti, Sayı:",sayı)
        break

