birler = ["","Bir", " İKi", "Üç", "Dört", "Beş","Alt","Yedi","Sekiz","DOkuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","YEtmiş","Seksen","Doksan"]
def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10
    return "{} {}".format(onlar[ikinci],birler[birinci])
sayı = int(input("Sayı:"))
print(okunus(sayı))