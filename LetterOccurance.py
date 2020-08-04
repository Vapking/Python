str = input("Enter A String :")

char = input("Enter Character/Letter to Search in String :")

count = 0 

for i in range(0,len(str)):
    if char==str[i]:
        count = count+1
        
print("Character is ",char," is Present :",count)