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
print(n_2d[:,1:3])
