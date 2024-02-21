import numpy as np
distance=[10,15,17,26]
time=[0.3,0.47,0.55,1.20]
# speed=distance/time # list operations not allowed in python, hence we use numpy arrays...
np_distance=np.array(distance)
np_time=np.array(time)
np_speed=np_distance/np_time
print(np_speed)

# Classes and Attributes of n-dimentional Array
np_city=np.array(['NYC','LA','Miami','Pataya','Moscow','Canberra'])
print("Dimension of array: ",np_city.ndim) # .ndim is an attribute which tells us the dimensions of the array...
city_with_state=np.array([['Gaya','Ayodhya','Jalandhar','Bhopal'],['Bihar','UP','Punjab','MP']])
print("Dimension of array:",city_with_state.ndim)
print("Shape of the Array",city_with_state.shape)
# shape,size,ndim and dtype are nd-array attributes...
# Basic Operations on array...
l1=[13,56,75,34]
l2=[12,54,87,77]
n_l1=np.array(l1)
n_l2=np.array(l2)
#Basic Ops on Arrays
n=n_l1+n_l2
print(n)
n=n_l1-n_l2
print(n)
n=n_l1*n_l2
print(n)
n=n_l1/n_l2
print(n)
n=n_l1%n_l2
print(n)
n=n_l1//n_l2
print(n)

# Bitwise Ops
n=n_l1&n_l2
print(n)
n=n_l1|n_l2
print(n)
n=~n_l2
print(n)
n=n_l1^n_l2
print(n)

# Accessing Array Elements
first=[10,15,35,54]
second=[12,43,21,37]
n_2d=np.array([first,second])
print(n_2d[0])
print(n_2d[1])
print(n_2d[1][3])
print(n_2d[:,1])
print(n_2d[:,1:3]) # nd_array[rows,column]


# Access elements: Iteration 
print("Array using iteration:")
print(n_2d.size)
for i in n_2d:
    print(i)

n_2d_rows=n_2d.ndim 
print(n_2d_rows)
n_2d_columns=n_2d[0].size
print(n_2d_columns)
for i in range(2):
    for j in n_2d[i]:
        print(j,end=" ")
print("\n")

#indexing with boolean Arrays
test_scores=np.array([[83,71,57,63],[54,68,81,45]])
pass_score=test_scores>60
print("Boolean Array:-\n",pass_score)
passed_Students_score=test_scores[pass_score]
print("Passed Student Scores:-\n",passed_Students_score)

#Copy and views
np_arr1=np.array([1,2,3,4,5])
np_arr2=np_arr1 #copying arr1 to arr2 by assignment. This creates same object as orignal array and change in one do not affects other
print(np_arr1 is np_arr2)

#View or Shallow Copy
np_arrView=np_arr1.view()
print(np_arrView)
print(np_arrView is np_arr1)# View creates a copy of the array as another object but change in view array also reflects to orignal array
print(len(np_arrView))
# Making Changes in View
np_arrView[4]=7
print(np_arrView)
print(np_arr1)# Orignal Data also gets change if we change the element in view

#Deep Copy: Where orignal Array is preserved
n_arrDeep=np_arr1.copy()
print(n_arrDeep is np_arr1) #array copied but returns false as copy function creates different objects with same element and change in copy array do not change orignal array


# Math functions in numpy
# sqrt,cos,floor,exp

np_dist=np.array([4,9,16,25,36,49,64,81,100])
np_sqrt=np.sqrt(np_dist)
print(np_sqrt)
print(np.pi)
from numpy import pi
print("Sin(pi/2):",np.sin(pi/2))
print("cos(pi/2):",np.cos(pi/2))
np_array=np.array([1.3,2.5,4.7])
print("Floor Values: ",np.floor(np_array))
print("e^element: ",np.exp(np_array))


#Shape Manipulation
# ravel,split,flatten,resize,reshape,stack

#Flattening of array
print(n_2d)
print(n_2d.flatten())# 2d into flatten 1d like copy
print(n_2d.flatten().ndim)# 2d into flatten 1d
n_ravel=n_2d.ravel()
print(n_ravel) # Flattens but like view means changes in ravel array also changes the orignal array
n_ravel[6]=8
print(n_ravel) 
print(n_2d)  

n_reshape=n_2d.reshape(8,1) # multiplication of elements should be equal to number of elements
print(n_reshape)

print(np.hsplit(n_2d,4))

print(np.hstack((n_2d,n_2d)))#dimensions of both the array should be same to be stacked together



