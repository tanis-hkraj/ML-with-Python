import numpy as np
list1=[1,34,56]
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
print(np.dot(marr,arr.reshape(3,1)))