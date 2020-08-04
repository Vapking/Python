from numpy import *

arr = array([2,4,7,21,56,521,123,3412,1,343,223])
print(arr)

# Finding Maximum Number From an Array
MaxNumber = arr[0]
for i in range(1,len(arr)):
    if MaxNumber < arr[i]:
        MaxNumber = arr[i] 

print("Maximum Number is :",MaxNumber)

# Finding Minmum Number From an Array
MinNumber = arr[0]
for i in range(1,len(arr)):
    if MinNumber > arr[i]:
        MinNumber = arr[i] 

print("Minimum Number is :",MinNumber)
