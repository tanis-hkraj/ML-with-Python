import numpy as np
list1=[1,34,56,76,89,76]
list2=[45,67,48,97,77,56]
list3=[34,87,64,63,21,32]
arr1=np.linspace(23,96,6,dtype=int)
arr2=np.linspace(45,76,6,dtype=int)
arr3=np.linspace(56,93,6,dtype=int)
marr2=np.array([arr1,arr2,arr3]).reshape(18,1)
marr1=np.array([list1,list2,list3]).reshape(1,18)
print(marr1)
print(marr2)
print(np.dot(marr1,marr2))
