import sys
from time import time, clock

def theta(x1,x2):
    dx = float(x1[0] - x2[0]); dy = float(x1[1] - x2[1]);
    if (abs(dx) < 1.e-6 and abs(dy) < 1.e-6):
        t = 0
    else:
        t = dy / (abs(dx) + abs(dy))
    if (dx < 0):
        t = 2 - t
    elif (dy < 0):
        t = 4 + t
        
    return float(t * 90)


result = []; f = open(sys.argv[1]); total_num = int(f.readline());

while total_num != 0:
    a = (f.readline().split())
    a = (int(a[0]), int(a[1]))   #  a[0] for X    a[1] for Y
    result.append(a); total_num -= 1;


i = 0; v = 0; pi = result[i]; last_angle = 0; k = 0;
test = []
A=[]
while k != len(result) and i != len(result):
    
    result[i],result[k] = result[k],result[i]
    minAngle = 360
    for x in range(i+1, len(result)):
        
        angle = theta(result[i], result[x])
        
        #A.append(angle) #will return all angles and it's float
        
        if (angle < minAngle) and (angle >= last_angle):
            minAngle = angle; k = x;
            test.append(k)

            
    i += 1; last_angle = minAngle;
    
    #print (k)
print (k)
#print (test[-2],test[-3],test[-1])
print (test)
#print (A[11], A[14],A[45])
#print (result[k])
    
t=clock()
print ('CPU time: ', clock()-t)







#while total_num != 0:
    #a = (f.readline().strip('\n')).split()
    #a = (int(a[0]), int(a[1]))
    #Num.append(a)
    #total_num=total_num-1

#print (Num[0][0])

#n = int(f.readline())
#l = f.readline()



