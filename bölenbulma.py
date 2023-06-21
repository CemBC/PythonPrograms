def tambölen(sayı):
    list = [1,sayı]
    for i in range(2,sayı):
        if sayı % i == 0:
            list.append(i)
    list.sort()
    return print("Bu sayının pozitif tam bölenleri :",list)
while True:
    sayı = int(input("Sayıyı giriniz:"))
    tambölen(sayı)
