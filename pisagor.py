def pisagor():
    for i in range(1,101):
        for j in range(1,101):
            for x in range(1,101):
                if i**2 + j**2 == x**2:
                    print("{},{},{} üçgeni bir pisagor üçgenidir.".format(i,j,x))
pisagor()

