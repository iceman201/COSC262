#Monotone Chain Convex Hull
import sys;
from time import time, clock

result = []; f = open(sys.argv[1]); total_num = int(f.readline());

while total_num != 0:
    a = (f.readline().split())
    a = (int(a[0]), int(a[1]))   #  a[0] for X    a[1] for Y
    result.append(a); total_num -= 1;
    
t=clock()
def Directed_Line_Segment(x1,x2,x3):
    x_a = x1[0]; x_b = x2[0]; x_c = x3[0]
    y_a = x1[1]; y_b = x2[1]; y_c = x3[1]
    
    Directed_Line_Segment = ((x_b - x_a) * (y_c - y_a)) - ((y_b - y_a) * (x_c - x_a))
    return Directed_Line_Segment

def convex_hull(result):
    result = sorted(set(result))
    if len(result) <= 1:
        return result
    LW = []; UP = []
    for i in result:
        while len(LW) >= 2 and Directed_Line_Segment(LW[-2], LW[-1], i) <= 0:
            LW.pop()
        LW.append(i)
    for y in reversed(result):
        while len(UP) >= 2 and Directed_Line_Segment(UP[-2], UP[-1], y) <= 0:
            UP.pop()
        UP.append(y)
    return LW[:-1] + UP[:-1]

print (convex_hull(result))
#
# the real computing time should be after finish calculating the points
# which is not include that index transction part so time counter should
# put before the index transction part.
# 
print ('CPU time: ', clock()-t)

#  Translate the point coordinates to the key of original table
result1=[]; UP = convex_hull(result)

for i in UP:
    if len(result1) == 0:
        result1.append(result.index(UP[0]))
    elif result.index(i) not in result1:
        result1.append(result.index(i))
print (result1) #index



