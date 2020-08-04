def LinearRecursiveSearch(searchList,index,NumberToFind):

    if index >= len(searchList):
        return print("Number Not Found!")
    
    if searchList[index] == NumberToFind:
        return print("\n Number is Find at Position : ",index + 1)
    
    return LinearRecursiveSearch(searchList,index+1,NumberToFind)

searchList = [5,12,8,7,19,25,67,52,81,72]
print(searchList)
NumberToFind = int(input("Enter Value to find :"))

LinearRecursiveSearch(searchList,0,NumberToFind)