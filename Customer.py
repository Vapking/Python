num = int(input("Enter Range till Find Profit :"))
total_profit=0
for i in range(1,num+1):
    profit = float(input("Profit :\n"))
    fraction = float(input("Fraction :\n"))
    mul = profit*fraction
    total_profit = total_profit+mul
print("\n\n**** Total Profit ****\n")
print(total_profit)