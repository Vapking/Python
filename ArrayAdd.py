from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([2,5,6,4,2])

# Adding two Array Without Using For Loop 
arr3 = arr1 + arr2
print(arr3)

# Using For Loop
arr4 = array([],int)
count = 0
for i in arr1:
       num = i + arr2[count]
       arr4 = append(arr4,num)
       count+=1
print(arr4)

