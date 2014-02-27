# This is quicksort
# sort(left,right) sorts array a from position left to right
# partition(left,right) partitions array a from position left to right
# with pivot x=a[left], and returns m such that after partition
# a[left .. m-1] <= x=a[m] <= a[m+1 .. right]

import random

from time import time, clock
Counter=0

def out(n):
  for i in range(1, n+1): print a[i],
  print '\n'

def sort(left,right):
  if left<right:
    m=partition(left,right)
    sort(left,m-1)
    sort(m+1,right)

def partition(left,right):      ## x is the pivot
  global Counter
  x=a[left]; i=left; j=right+1  ## i goes right, j goes left           
  while i<j:
    j=j-1; 
    if i==j: 
      break
    while a[j]>=x:          ## while a[j]>=x, 
      Counter += 1
      j=j-1;                ## j goes left
      if i==j : break
    if i==j: break
    a[i]=a[j]               ## a[j] is copied to a[i]
    i=i+1
    if i==j: break
    while a[i]<=x:          ## while a[i]<=x,
      Counter += 1
      i=i+1;                ## i goes right
      if i==j : break
    if i==j: break
    a[j]=a[i]               ## a[i] is copied to a[j]
  a[i]=x                    ## pivot x settles down at i
  return i  

# {main program}
n=input('input n ')
a=[]
for i in range(0,n+1): a=a+[int(100*random.random())] 
t=clock()
sort(1,n)
out(n)
print 'CPU time: ',clock()-t
print "Number of Comparesions: ", Counter
n=raw_input('finished ')