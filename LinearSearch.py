def search(key):
    for i in List:
        if(i==key):
            print("Number Found!")
            break
    else:
        print("Number not Found!")

List=[5,12,8,7,19,25,67,52,81,72]

print(List)

num = int(input("Enter Number to Find :"))

search(num)