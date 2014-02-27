# This is heapsort
# sort() sorts array a in descending order
# sift(p,q) heapifies array a from position p to q
# heap is a max-heap, that is, maximum at the root

import random
Counter=0
from time import time, clock
def out(n):
  for i in range(1, n+1): print a[i],
  print '\n'

def swap(i,j): # This swaps a[i] and a[j]
  w=a[i]; a[i]=a[j]; a[j]=w

def siftup(p, q):      # This is to heapify a when a[p] is wrong
  global Counter
  y=a[p]; j=p; k=3*p-1  # a[p] is saved to y
  k_mid = k+1; k_right = k+2
  while k <= q :
    z=a[k]
    Counter += 1
    if k_mid <= q:
      Counter += 1
      if z > a[k_mid]:
        z=a[k_mid]
        k=k_mid
      
    if k_right <= q:
      Counter += 1
      if z > a[k_right]:
        z = a[k_right]
        k = k_right
        
    if y <= z :break 
    a[j]=z;j=k;k=3*j-1; k_mid=k+1; k_right=k+2
  a[j]=y               # y settles down at position j

def build_heap(n):
  for i in reversed(range(1,(n+1)/3)): siftup(i, n)
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
sort()
out(n)
print 'CPU times: ',clock()-t
print 'Number of comparisons: ',Counter
n=raw_input('finished ')