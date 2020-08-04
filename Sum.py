NumberOfIteration = int(input("Enter Number of Iteration for Sum :"))

NumberOfStart = int(input("Enter Number of Start for Sum :"))

sum = 0
for i in range(1,NumberOfIteration+1):
    for j in range(NumberOfStart,0,-1):
        sum += j
    NumberOfStart = sum
print("Sum of Number For ",NumberOfIteration," is : ",sum)
