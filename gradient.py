import sys

x=0
y=0
l=-.01

def functionA(x,y): #returns dx and dy
    #4x^2 -3xy +2y^2 +24x -20y
    dx=8*x-3*y+24
    dy=-3*x+4*y-20
    return dx,dy

def functionB(x,y):
    #(1-y)^2+(x-y^2)^2
    dx=2*(x-y**2)
    dy=2*(-2*x*y+2*y**3+y-1)
    return dx,dy


if sys.argv[1]=="A":
    dx, dy = 100, 100
    while (dx ** 2 + dy ** 2) ** .5 > 10 ** -8:
        dx, dy = functionA(x, y)
        x += l * dx
        y += l * dy
        print("Location: " + str((x, y)))
        print("Gradient: " + str((dx, dy)))
else:
    dx, dy = 100, 100
    while (dx ** 2 + dy ** 2) ** .5 > 10 ** -8:
        dx, dy = functionB(x, y)
        x += l * dx
        y += l * dy
        print("Location: " + str((x, y)))
        print("Gradient: " + str((dx, dy)))