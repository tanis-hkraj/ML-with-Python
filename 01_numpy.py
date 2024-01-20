import numpy as np
my_lst=[1,2,3,4,5,6,7]
arr=np.array(my_lst)#np.array(<list>): Used to convert a list into n dimension array.
print(type(arr))
print(arr)
print(arr.shape)#arr.shape : tells us the dimensions of the array <number of rows and column>
my_lst1=[1,2,3,4,5,6,7]
my_lst2=[8,9,10,11,12,13,14]
my_lst3=[15,16,17,18,19,20,21]
arr1=np.array([my_lst1,my_lst2,my_lst3])#creating a 2d array
print(arr1)
print(type(arr1))
print(arr1.shape)
print(arr1.reshape(7,3))
print(arr1)
print(arr1[1:,5:])

arr2=np.arange(0,100,step=2)#np.arrange(start,end,step): creates an 1D array have elements from start to end and step skip the numbers between elements
print(arr2)
arr2=np.linspace(1,50,10)#np.linspace(start,end,number of division): creates a 1D of numbers from start to end with given number of divisions...
print(arr2)
#broadcasting : converting a particular range of elements to a particular element
arr2[5:8]=100
print(arr2)
print(arr1>6)
print(arr1/6)
print(arr1+6)
print(arr1-6)
print(arr1*6)
#copying an array
arr3=arr2
arr3[1:5]=20
print(arr3)
arr4=np.arange(0,20).reshape(4,5)
arr5=np.arange(20,40).reshape(4,5)
arr6=arr4*arr5
print(arr6)

print(np.ones(5,dtype=int))
print(np.ones((3,5),dtype=int))
arr6[0,0]=1
print(arr6.sum())#sum of all elements
print(arr6.ndim)#returns dimension whenther 1d 2d or 3d and so on.
print(arr6.size)#number of elements in an array
print(np.ones((5,4,6),dtype=int))
print(np.zeros((3,4)))#array with all 0s
print(np.full((3,4),6,dtype=int))
print(np.full((3,4),7,dtype=float))
print(np.full((3,4),8+6j,dtype=complex))
print(arr6.flatten())#compress the array in 1D
print(arr6.T)#converts the array to its transpose
print(arr6)
arr6.sort()
print(arr6)