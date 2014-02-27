# This is heapsort
# sort() sorts array a in descending order
# siftup(p,q) heapifies array a from position p to q
# heap is a min-heap, that is, minimum at the root
import random
from time import time, clock
c=0
def out(n):
    for i in range(1, n+1): print a[i],
    print '\n'
def swap(i,j): # This swaps a[i] and a[j]
    w=a[i]; a[i]=a[j]; a[j]=w
def siftup(p, q): ## This heapifies array a from position p to q
    y=a[p]; j=p; k=2*p ## a[p] is saved to y, 
    global c
    while k <= q :
        z=a[k]
        c+=1
        if k < q :
            c+=1
            if z > a[k+1]: ## Choose the child with smaller value
                k=k+1 
                z=a[k] ## z is to hold the smaller value
        if y <= z : break
        a[j]=z; j=k; k=2*j
    a[j]=y ## y settles down at position j
def build_heap(n):
    for i in reversed(range(1,n/2+1)): siftup(i, n)
def sort():
    build_heap(n)
    for i in reversed(range(2,n+1)) :
        swap(1, i) # swap a[1] and a[i]
        siftup(1,i-1) # Heapify a from position to position i-1
# {main program}
n=input('input n ')
a=[]
for i in range(0,n+1): a=a+[int(100*random.random())]
t=clock()
sort(); out(n)
print 'CPU time ',clock()-t
print "Number of comparisons: ", c
n=raw_input('finished ')