def search(key):

    flag = 0 
    beg = 0 
    end = len(List)-1

    while(beg<=end):
        
        mid = (beg+end)//2
        
        if(key == List[mid]):
            flag = 1
            break
        
        if(key<List[mid]):
            end = mid-1
        else:
            beg = mid+1
    
    if(flag == 1):
        print("Number is Found ",key," at Location ",mid-1)
    else:
        print("Number not Found!")

List = [5,12,8,7,19,25,67,52,81,72]
List.sort()

print(List)
NumberToFind = int(input("Enter Number Want To Find ?\n"))

search(NumberToFind)