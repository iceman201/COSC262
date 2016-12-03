import sys
from time import time, clock

result = []; f = open(sys.argv[1]); total_num = int(f.readline());

while total_num != 0:
    a = (f.readline().split())
    a = (int(a[0]), int(a[1]))   #  a[0] for X    a[1] for Y
    result.append(a); total_num -= 1;
    
t=clock()

def distance(p, q):
    #distance between points p and q
    dx, dy = int(q[0]) - int(p[0]), int(q[1]) - int(p[1])
    return (dx * dx) + (dy * dy)

def turn(p, q, r):
    #returns -ve,0, or +ve depending on the angle p-q-r makes (with q being the angle)
    return ((int(q[0]) - int(p[0]))*(int(r[1]) - int(p[1])) - (int(r[0]) - int(p[0]))*(int(q[1]) - int(p[1])) > int(0)) - ((int(q[0]) - int(p[0]))*(int(r[1]) - int(p[1])) - (int(r[0]) - int(p[0]))*(int(q[1]) - int(p[1])) < int(0))

L_turn, R_turn, straight = (1, -1, 0)

def next_hull_point(points, p):
    #outputs the next hull point
    q = p
    for r in points:
        t = turn(p, q, r)
        if t == R_turn or t == straight and distance(p, r) > distance(p, q):
            q = r
    return q

def find_min_p(points):
    min_num = points[0]
    for i in points:
        if int(i[1]) < int(min_num[1]):
            min_num = i
        elif int(i[1]) == int(min_num[1]):
            if int(i[0]) < int(min_num[0]):
                min_num = i
    return min_num

def find_hull(points):
    min_p = find_min_p(points); hull = [min_p]
    for p in hull:
        q = next_hull_point(points, p)
        if q != hull[0]:
            hull.append(q)
    return hull

print (find_hull(result)) #points
#
# the real computing time should be after finish calculating the points
# which is not include that index transction part so time counter should
# put before the index transction part.
# 
print ('CPU time: ', clock()-t)

def hull_index(points,hull):
    result = []
    for i in hull:
        result.append(points.index(i))
    return result

print (hull_index(result,find_hull(result))) #index
