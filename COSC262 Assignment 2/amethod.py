import math
import sys

#hull = [(23.45, 57.39), (23.45, 60.39), (24.45, 63.39),
        #(26.95, 68.39), (28.45, 69.89), (34.95, 71.89),
        #(36.45, 71.89), (37.45, 70.39), (37.45, 64.89),
        #(36.45, 63.39), (34.95, 61.39), (26.95, 57.89),
        #(25.45, 57.39), (23.45, 57.39)]



result = []; f = open(sys.argv[1]); total_num = int(f.readline());

while total_num != 0:
    a = (f.readline().split())
    a = (int(a[0]), int(a[1]))   #  a[0] for X    a[1] for Y
    result.append(a); total_num -= 1;
hull = result

def mostfar(j, n, s, c, mx, my): # advance j to extreme point
    xn, yn = hull[j][0], hull[j][1]
    rx, ry = xn*c - yn*s, xn*s + yn*c
    best = mx*rx + my*ry
    while True:
        x, y = rx, ry
        xn, yn = hull[(j+1)%n][0], hull[(j+1)%n][1]
        rx, ry = xn*c - yn*s, xn*s + yn*c
        if mx*rx + my*ry >= best:
            j = (j+1)%n
            best = mx*rx + my*ry
        else:
            return (x, y, j)

n = len(hull)
iL = iR = iP = 1                # indexes left, right, opposite
pi = 4*math.atan(1)
for i in range(n-1):
    dx = hull[i+1][0] - hull[i][0]
    dy = hull[i+1][1] - hull[i][1]
    theta = pi-math.atan2(dy, dx)
    s, c = math.sin(theta), math.cos(theta)
    yC = hull[i][0]*s + hull[i][1]*c

    xP, yP, iP = mostfar(iP, n, s, c, 0, 1)
    if i==0: iR = iP
    xR, yR, iR = mostfar(iR, n, s, c,  1, 0)
    xL, yL, iL = mostfar(iL, n, s, c, -1, 0)
    area = (yP-yC)*(xR-xL)

    print ('    {:2d} {:2d} {:2d} {:2d} {:9.3f}'.format(i, iL, iP, iR, area))