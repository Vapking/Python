tup = (1,2,3,4)

while True:

    print("\n=============== MENU ================")
    print("1.Access Element")
    print("2.Location of Element")
    print("3.Length of Tuple")
    print("4.Minimum Element in Tuple")
    print("5.Maximum Element in Tuple")
    print("6.Sorted Tuple")
    print("7.Display")
    print("8.Exit")
    
    ch = int(input("Enter Your Choice :"))
    
    #Access Element
    if ch==1:
        index = int(input("Enter Loaction to get data = "))
        print("The Data at Location is = ",tup[index])
    #Location
    elif ch==2:
        data = int(input("Enter data to get Location = "))
        print("The Data is Present at Location = ",tup.index(data))
    #Length
    elif ch==3:
        length = len(tup)
        print("Length of Tuple is = ",length)
    #Minimum
    elif ch==4:
        print("Minimum Value in = ",min(tup))
    #Maximum
    elif ch==5:
        print("Maximum Value in = ",max(tup))
    #Sorted
    elif ch==6:
        sorted(tup)
        print("Sorted Tuple is = ",tup)
    #Display
    elif ch==7:
        print("Tuple = ",end= " ")
        for i in tup:
            print(i,end=" ")
    #Exit
    elif ch==8:
        print("Thank you !")
        break