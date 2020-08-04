n = int(input("Enter Number of Element for List=")) 
print("Enter Somthing in lst")
lst = []

for i in range(0,n):
    data = input()
    lst.append(data)
print(lst)

while True:
    print("=============== MENU ================")
    print("1.Append in List")
    print("2.Extend List")
    print("3.Insert in List")
    print("4.Count of Element in List")
    print("5.Location of Data in List")
    print("6.Revers List")
    print("7.Sort List")
    print("8.Remove an Object from List")
    print("9.Pop Last Element form List")
    print("10.Create Duplicate Copy of List")
    print("11.Clear Whole List")
    print("12.Exit")

    ch = int(input("Enter Your Choice :"))

   #Append
    if ch==1:
        data = input("Enter Somthing to Add =")
        lst.append(data)
        print("After Appeding the Element \n",lst)
    #Extend
    elif ch == 2:
        Num = input("Enter Extend Value =")
        lst.extend(Num)
        print("After Extending List \n",lst)
    #Insert 
    elif ch == 3:
        index = int(input("Enter Index Number to insert the data = "))
        data = input("Enter Data to Insert =")
        lst.insert(index,data)
        print("After Insertion \n",lst)
    #Count
    elif ch == 4:
        Num = input("Enter Value to Get Count =")
        print("Count of Number Occured in the list=",lst.count(Num))
    #Index   cle
    elif ch == 5:
        index = input("Enter Data get Index =")
        print("Element Present at Location :",lst.index(index))
    #Reverse
    elif ch == 6:
        list = lst
        list.reverse()
        print("After Reversing List =",list)
    #Sort
    elif ch == 7:
        list = lst
        list.sort()
        print("After Sorting List=",list)
    #Remove
    elif ch == 8:
        Num = input("Enter Data to remove =")
        print("After Removing given Element=",lst.remove(Num))
    #pop
    elif ch == 9:
        print("After Poping the Element = ",lst.pop())
        #Copy
    elif ch == 10:
        list2 = lst.copy()
        print("Original List :\n",lst)
        print("Duplicate List :\n",list2)
    #clear
    elif ch == 11:
        list = lst
        print("List Has been Cleared!",list.clear())
    #Exit
    elif ch == 12:
        print("Thank You!")
        break


