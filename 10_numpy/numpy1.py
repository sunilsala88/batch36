
import numpy as np
l1=[1,2,3,4.4]
print(l1)
arr=np.array(l1)
print(arr)

ar1=np.zeros(5,dtype=int)
print(ar1)
ar2=np.ones(10,dtype=int)
print(ar2)
ar3=np.arange(100,200)
print(ar3)

a=[[1,2,3],[4,5,6],[7,8,9]]
print(a)
np1=np.array(a)
print(np1)
print(np1[1,1])
np2=np.arange(25,50).reshape(5,5)
print(np2)
print(np2[4,3])