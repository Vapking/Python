def Zero():
    try:
        No1 = int(input("Enter Number No1="))
        No2 = int(input("Enter Number No2="))
        print("Division is = ",No1/No2)
    except ZeroDivisionError:
        print("ZeroDivisionError Occurs !\n")    

def Type():
    try:
        No1 = input("Enter a Number No1=")
        No2 = input("Enter a Number No2=")
        print("Addition is = ",No1 + int(No2))
    except TypeError:
        print("TypeError Occurs!\n")

def Value():
    try:
        No1 = input("Enter a Number No1=")
        No2 = input("Enter a Number No2=")
        print("Addition is = ",int(No1) + int(No2))
    except ValueError:
        print("ValueError Occurs!\n")

def Name():
    try:
        No1 = input("Enter a Number No1=")
        No2 = input("Enter a Number No2=")
        print("Addition is = ",int(No) + int(No2))
    except NameError:
        print("NameError Occurs!\n")

def Index():
    try:
        List = [1,2,3,4]
        print("Element at Location 4=",List[4])
    except IndexError:
        print("\nIndexError Occurs!")
    
def Key():
    try:
        Dict = {'1':"Ram",'2':"Raju",'3':"Roy"}
        print("Value of Key 4 =",Dict[4])
    except KeyError:
        print("\nkeyError Occurs!")

Zero()
Type()
Value()
Name()
Index()
Key()


    