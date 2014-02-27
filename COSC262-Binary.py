from time import clock, time
from random import random
## This is to insert into a binary search tree by Python objects 
###
####################### tree #########################
# 6 3 1 4 5 2 6 #
# 3 #
# 1 4 #
# 2 5 #
######################################################
Counter=0
class node:
    key=0
    left=0
    right=0

def insert(x) :
    global Counter
    p=root
    while p!=0 :
        Counter+=1
        q=p
        if x<=p.key:
            p=p.left
        else: p=p.right
    p=node()
    p.key=x; 
    if x<=q.key: 
        Counter+=1
        q.left=p # p inserted to the left of q
    else: q.right=p # p inserted to the right of q

def traverse(p):
    if p!=0:
        p1=p.left
        traverse(p1)
        t.append(p.key)
        p2=p.right
        traverse(p2)

n=int(input('input n '))
t=[]
for i in range(0,n): t=t+[random()]; 
n=len(t)
tt=clock()
x=t[0]
root=node(); node.key=x; node.right=0; node.right=0;
for i in range(1,n):x=t[i];insert(x)
traverse(root)
tt=clock()-tt
print ("CPU times: ", tt)
print ('Number of Comparesions: ', Counter)
print ("Finished")
