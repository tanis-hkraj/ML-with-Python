import numpy as np
list1=[1,2,3]
arr=np.array([list1])
arr1=np.linspace(1,10,3,dtype=int)
print(arr1)
marr=np.array([arr1])
print(arr)
a=5
b=3
print(arr*a)
print(arr+a)
print(arr-a)
print(arr/a)
print(arr%a)
# print(arr.reshape(6,3))
print(a*arr+b*marr)
print(np.dot(marr,arr.T))
print(arr@marr.T)#dot product shortcut...
arr=arr.T
#vector norm
arr=np.array([[3],[-4],[-9]]);
# 1. Euclidean Norm
n=np.linalg.norm(arr,2)
print(n)
# 2. Manhattar Norm
n=np.linalg.norm(arr,1) 
print(n)
# 3. Max Norm
n=np.linalg.norm(arr,np.inf)
print(n)
