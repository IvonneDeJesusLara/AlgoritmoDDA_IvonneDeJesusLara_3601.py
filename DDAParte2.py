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
    for i in range (x, steps):
        plt.plot(round(x1), round(y1), marker="s", color="black")
        x1= x1+incx
        y1= y1+incy
        print (x1, ',', y1)
    plt.show()