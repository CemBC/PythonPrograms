while True:
    toplam = 0
    a = input("Sayıyı giriniz:")
    b = len(a)
    c = int(a)
    for i in range(0,b):
        toplam += int(a[i])**b
    if toplam == c:
        print("Sayınız bir armstrong sayısı.")
    else:
        print("Sayınız bir armstrong sayısı değil.")




