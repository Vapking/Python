from numpy import *

# Without Using Any Method Coping An Array
arr1 = array([6,2,3,5,7,8])
arr2 = arr1

print("Array 1 :",arr1)
print("Array 2 :",arr2)

print("Memory Address of Array 1 :",id(arr1))
print("Memory Address of Array 2 :",id(arr2))

# Shallow Copy 
arr2 = arr1.view()

arr1[1] = 4

print("Array 1 :",arr1)
print("Array 2 :",arr2)

print("Memory Address of Array 1 :",id(arr1))
print("Memory Address of Array 2 :",id(arr2))

# Deep Copy 

arr2 = arr1.copy()

arr1[1] = 2

print("Array 1 :",arr1)
print("Array 2 :",arr2)

print("Memory Address of Array 1 :",id(arr1))
print("Memory Address of Array 2 :",id(arr2))
