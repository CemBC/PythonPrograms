a = int(input("Sayıyı giriniz:"))
toplam = 0
for i in range(1, a):
    if a% i == 0:
        toplam += i
if toplam == a:
    print("Girdiğiniz değer bir mükemmel sayı.")
else:
    print("Girdiğiniz deper bir mükemmel sayı değil.")