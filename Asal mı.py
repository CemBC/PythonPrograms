def asal_sayı(sayı):
    if sayı == 1 :
        return "Asal Değil."
    elif sayı == 2:
        return "Asal."
    else:
        for i in range(2,sayı):
            if sayı % i == 0:
                return "Asal değil."
            return "Asal."
while True:
    sayı = input("Sayı:")
    if sayı == "q":
        print("Programdan çıkış yapılıyor.")
        break
    else:
        sayı = int(sayı)
        print(asal_sayı((sayı)))



