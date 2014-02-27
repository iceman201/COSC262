# This is alternate mergesort
# mergesort(p,q) sorts array a from position p to q
# This is alternate mergesort 
import random
from time import time, clock
c=0
t=clock()
def out(a, n):
    for i in range(1, n+1): print (a[i],)
    print ('\n')
def mergesort(p, q, t): ## parameter t controls switching between merge1 and
    if p < q : ## merge2
        m = (p+q) / 2
        mergesort(p, m, -t); # t alternates between + and -
        mergesort(m+1, q, -t); # meaning merge1 and merge 2 alternate
        if t>0 : 
            merge1(p, m+1, q+1) # from level to level in recursion.
        else:         
            merge2(p, m+1, q+1)
    # merge(p,m+1,q+1) merges the portion of array a from position p to m
    # and that from position m+1 to q
def merge1(p, r, q): ## This is the original merge from a to b
    global c
    i=p; j=r; k=p;
    while i < r and j < q :
        c=c+1
        if a[i] <= a[j]:
            b[k] = a[i]; i=i+1 
        else : b[k] = a[j]; j=j+1 
        k=k+1
    while i < r :
        b[k]= a[i];
        i=i+1; k=k+1
    while j < q :
        b[k] = a[j];
        j=j+1; k=k+1
def merge2(p, r, q): # This is the merge from b to a
    global c
    i=p; j=r; k=p;
    while i < r and j < q :
        c=c+1
        if b[i] <= b[j]:
            a[k] = b[i]; i=i+1 
        else : a[k] = b[j]; j=j+1 
        k=k+1
    while i < r :
        a[k]= b[i];
        i=i+1; k=k+1
    while j < q :
        a[k] = b[j];
        j=j+1; k=k+1
#{ main program }    
n=input('input n ')
a=[]
for i in range(0,n+1): a=a+[int(100*random.random())]
b=[]
for i in range(0,n+1): b=b+[a[i]]
mergesort(1, n, 1)
out(b, n)
print ('CPU time: ',clock()-t)
print ('Number of Comparesions: ',c)
n=raw_input('finished ')