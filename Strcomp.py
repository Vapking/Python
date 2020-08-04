#enter two string and display which string is larger

str1 = input("Enter 1st String :")
str2 = input("Enter 2nd String :")

no1 = len(str1)
no2 = len(str2)

if no1>no2:
 print("String :",str1," is Large!")
elif no1==no2:
 print("Strings are Equal!")
else:
 print("String :",str2," is Large!")
