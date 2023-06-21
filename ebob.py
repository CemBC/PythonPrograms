def ebob(a,b):
    liste = [a,b]
    liste.sort()
    liste1 = []
    for i in range(1,liste[0]+1):
        if (a % i ==0) and (b % i == 0):
            liste1.append(i)
            liste1.sort()
    return liste1[-1]
while True:
    a = int(input("Sayı-1:"))
    b = int(input("Sayı-2:"))
    print("Sayırların EBOB' u :",ebob(a,b))