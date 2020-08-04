M1,M2,M3 = input("Enter Marks of Three Subject : ").split(" ")

Sum_Of_Marks = int(M1)+int(M2)+int(M3)

print("Sum of Marks : ",Sum_Of_Marks)

Percentage_Of_Marks = (Sum_Of_Marks/300)*100

print("Percentage of Marks : ",Percentage_Of_Marks)

if Percentage_Of_Marks > 90:
	print("Distinction")
elif Percentage_Of_Marks < 91 and Percentage_Of_Marks > 70:
	print("First Class") 
elif Percentage_Of_Marks < 71 and Percentage_Of_Marks > 50:
	print("Second Class")
elif Percentage_Of_Marks < 51 and Percentage_Of_Marks > 45:
	print("Pass")
else:
	print("Fail")

print("Executed!")