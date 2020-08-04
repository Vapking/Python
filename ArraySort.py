from array import *

vals = array('i',[5,6,4,3,7,2])

for i in range(len(vals)):
    
    for j in range(len(vals)-1):
        if vals[j]>vals[j+1]:
            tmp = vals[j]
            vals[j] = vals[j+1]
            vals[j+1] = tmp

for num in vals:
    print(num)