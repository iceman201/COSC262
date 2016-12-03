import sys;
from time import time, clock

result = []; f = open(sys.argv[1]); total_num = int(f.readline());
other_result = []
while total_num != 0:
    a = (f.readline().split())
    a = (int(a[0]), int(a[1]))   #  a[0] for X    a[1] for Y
    result.append(a); other_result.append(a); total_num -= 1;
    
    
t=clock() 
def Directed_Line_Segment(x1,x2,x3):
    x_a = x1[0]
    x_b = x2[0]
    x_c = x3[0]
    y_a = x1[1]
    y_b = x2[1]
    y_c = x3[1]
    l = ((x_b - x_a) * (y_c - y_a)) - ((y_b - y_a) * (x_c - x_a))
    return l

def Graham_scan(result):
    UP = []; LW = []; result.sort()
    for p in result: 
        while len(UP) > 1 and Directed_Line_Segment(UP[-2], UP[-1], p) <= 0: 
            UP.pop() 
        while len(LW) > 1 and Directed_Line_Segment(LW[-2], LW[-1], p) >= 0: 
            LW.pop() 
        UP.append(p)
        LW.append(p)
    return UP + LW

print (Graham_scan(result)) #points

#
# the real computing time should be after finish calculating the points
# which is not include that index transction part so time counter should
# put before the index transction part.
# 
print ('CPU time: ', clock()-t) 

# The code shows below is for translate points to the index of the list
# Order would be different but the result is correct as expected
Total_point = set(Graham_scan(result))
result1 = []
for i in Total_point:
    result1.append(other_result.index(i))

print (result1) #index
