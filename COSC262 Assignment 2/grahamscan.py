import sys;
from time import time, clock


result = []; f = open(sys.argv[1]); total_num = int(f.readline());

while total_num != 0:
    a = (f.readline().split())
    a = (int(a[0]), int(a[1]))   #  a[0] for X    a[1] for Y
    result.append(a); total_num -= 1;
    
def left(x1,x2,x3):
    x_a = x1[0]
    x_b = x2[0]
    x_c = x3[0]
    y_a = x1[1]
    y_b = x2[1]
    y_c = x3[1]
    
    l = ((x_b - x_a) * (y_c - y_a)) - ((y_b - y_a) * (x_c - x_a))
    return l

#def orientation(p, q, r):
    #return (q[1]-p[1])*(r[0]-p[0]) - (q[0]-p[0])*(r[1]-p[1])
           
U = [] 
L = []
result.sort()
    
for p in result: 
    while len(U) > 1 and left(U[-2], U[-1], p) <= 0: 
        U.pop() 
    while len(L) > 1 and left(L[-2], L[-1], p) >= 0: 
        L.pop() 
    U.append(p)
    L.append(p)
        
print (U,L)

t=clock()
print ('CPU time: ', clock()-t)