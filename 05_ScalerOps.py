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


#distance between two vectors
x,y=np.array([[2],[0]]),np.array([[0],[2]])
distance=np.linalg.norm(x-y,2)

#Angle between two vectors
cos_theta=(x.T@y)/((np.linalg.norm(x,2))*np.linalg.norm(y,2))
print(cos_theta)
angle=np.arccos(cos_theta)
degree=angle*(180/np.pi)
print(degree)