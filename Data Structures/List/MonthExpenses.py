month_expenses = [2200,2350,2600,2130,2190]
print("I Spent extra ",(month_expenses[1]-month_expenses[0]),"$ Feb Compare Jan.",sep="")
print("Total Expenses Of First Quarter is ",(month_expenses[0]+month_expenses[1]+month_expenses[2]),"$ .",sep="")

for i in range(len(month_expenses)):
    if month_expenses[i] == 2000:
        print("Yes in ",i+1,"Month.")
        break
else:
    print("Not in any Month.")
    
month_expenses.append(1980)
for i in month_expenses:
    print(i,end=" ")

print()

month_expenses[3]+=200
for i in month_expenses:
    print(i,end=" ")
