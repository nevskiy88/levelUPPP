import math
def deskriminant(a, b, c):

    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (- b + math.sqrt(D)) / (2 * a)
        x2 = (- b - math.sqrt(D)) / (2 * a)
        print(x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print("нет корней")


a = int(input())
b = int(input())
c = int(input())
arguments = deskriminant(a,b,c)