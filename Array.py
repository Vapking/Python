from numpy import *

# Creating Array Using array() Method
arr1 = array([1,2,3,4,5.3],int)

print("Array1 :",arr1)
print("Array1 Type :",arr1.dtype)

# Creating Array Using linspace() Method
arr2 = linspace(0,10,5)

print("Array2 :",arr2)

# Creating Array Using arange() Method
arr3 = arange(1,10,2)

print("Array3 is :",arr3)

# Creating Array Using logspace() Method
arr4 = logspace(1,40,5)

print("Array4 :",arr4)

# Creating Array Using zeros() & ones() Method
arr5 = zeros(5,int)
arr6 = ones(5,int)

print("Array5 :",arr5)
print("Array6 :",arr6)
