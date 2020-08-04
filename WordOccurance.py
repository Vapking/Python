str = input("Enter A String :")

str1 = str.split(" ")

searchstr = input("Enter word to check its Occurance :")

count = 0

for i in range(0,len(str1)):
    if searchstr==str1[i] :
        count = count + 1

print("String : ",searchstr," occured :",count)