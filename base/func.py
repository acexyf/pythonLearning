import math


def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x,y = move(100,100, 60, math.pi/6)
print(x,y)
print('')


def quadratic(a, b, c):
    x1 = 0
    x2 = 0
    if a == 0:
        x1 = -b/c
        x2 = -b/c
    else:
        delt = math.sqrt(math.pow(b, 2) - 4*a*c)
        x1 = (-1 * b + delt)/2/a
        x1 = (-1 * b - delt)/2/a
    return x1,x2


val1,val2 = quadratic(2,-4,2)

print(val1,val2)
print('')
