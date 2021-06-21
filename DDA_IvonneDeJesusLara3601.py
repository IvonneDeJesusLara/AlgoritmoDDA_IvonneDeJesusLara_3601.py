import matplotlib.pyplot as plt
def Graficar(x1, y1, x2, y2):
    x=0
    dx= abs(x2-x1)
    dy= abs(y2-y1)
    if dx > dy:
        steps= dx
    else:
        steps= dy

    incx= dx/steps
    incy= dy/steps
    for i in range (x, steps + 1):
        plt.plot(round(x1), round(y1), marker="s", color="black")
        x1= x1+incx
        y1= y1+incy
        print (round(x1), ',', round(y1))
    plt.show()


def main():
    x1= int(input('INGRESA VALOR PARA X1:\n'))
    y1= int(input('INGRESA VALOR PARA X2:\n'))
    x2= int(input('INGRESA VALOR PARA Y1:\n'))
    y2= int(input('INGRESA VALOR PARA Y2:\n'))

    Graficar(x1, y1, x2, y2)


if __name__== '__main__':
    main()

