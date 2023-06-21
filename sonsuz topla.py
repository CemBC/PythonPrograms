toplam = 0
while True:
    a = (input("Sayı:"))
    if a == "q":
        print("Toplamları:", toplam)
        break
    else:
        a = int(a)
        toplam += a