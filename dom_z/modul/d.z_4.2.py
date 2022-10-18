import math
import matplotlib.pyplot as plt
def deskriminant(a, b, c):

    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (- b + math.sqrt(D)) / (2 * a)
        x2 = (- b - math.sqrt(D)) / (2 * a)
        print(x1, x2)
        x0= -b / (2 * a)
        y0 = -D / 4 * a


        x_coords = [x2, x0, x1 ]  # координаты точек по оси Х
        y_coords = [0, y0, 0]  # координаты точек по оси Y
        plt.plot(x_coords, y_coords)
        plt.show()

    elif D == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print("нет корней")

a = int(input())
b = int(input())
c = int(input())
arguments = deskriminant(a,b,c)
