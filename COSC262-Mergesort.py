# This is mergesort. mergesort(p,q) sorts array a from position p to q
import random
from time import time, clock
c=0
def out(n):
 for i in range(1, n+1):print a[i]
print '\n'
def mergesort(p, q):
    if p < q :
        m = (p+q) / 2;
        mergesort(p, m);
        mergesort(m+1, q);
        merge(p, m+1, q+1) # This is to merge a[p .. m] and a[m+1 .. q] into b[p .. q]
def merge(p, r, q):
    global c ### c is comparison counter
    i=p; j=r; k=p;
    while i < r and j < q :
        c=c+1
        if a[i] <= a[j]:
            b[k] = a[i]; i=i+1 # if a[i]<=a[j] copy a[i] to b[k]
        else : b[k] = a[j]; j=j+1 # else copy a[j] to b[k]
        k=k+1
    while i < r : # Flash out the remaining elements in the left half to b
        b[k]= a[i]; i=i+1; k=k+1
    while j < q : # Flash out the remaining elements in the left half to b
        b[k] = a[j];
        j=j+1; k=k+1;
    for k in range(p,q): a[k] = b[k] 
# main program 
n=input('input n ')
a=[]
for i in range(0,n+1): a=a+[int(100*random.random())]
b=[]
for i in range(0,n+1): b=b+[0]
t=clock()
mergesort(1, n); out(n)
print 'time ',clock()-t, 'c=', 
print 'Comparisons: ',c
n=raw_input('finished ')