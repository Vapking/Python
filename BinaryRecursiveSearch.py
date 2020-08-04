def BinaryRecursiveSearch(searList,lowindex,highindex,NumberToFind):
    if lowindex > highindex:
        return print("Number Not Found!")
    else:
        mid = (lowindex+highindex)//2

        if NumberToFind == searchList[mid]:
            return print("\nNumber Find At Position : ",mid+1)
        elif NumberToFind<=searchList[mid]:
            return BinaryRecursiveSearch(searchList,lowindex,mid-1,NumberToFind)
        else:
            return BinaryRecursiveSearch(searchList,mid+1,highindex,NumberToFind)

searchList = [5,12,8,7,19,25,67,52,81,72]
searchList.sort()

print(searchList)
NumberToFind = int(input("Enter Number To Find in List :\n"))

BinaryRecursiveSearch(searchList,0,len(searchList)+1,NumberToFind)