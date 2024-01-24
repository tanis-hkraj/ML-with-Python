import numpy as np
list1=[1,34,56,76,89,76]
list2=[45,67,48,97,77,56]
list3=[34,87,64,63,21,32]
arr=np.array([list1,list2,list3])
print(arr)
a=5
print(arr*a)
print(arr+a)
print(arr-a)
print(arr/a)
print(arr%a)
print(arr.reshape(6,3))
