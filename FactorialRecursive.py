def fact(n):
    if n<=1:
        return 1
    else:
        result = n * fact(n-1)
    return result
    
n = int(input("Enter A Number :"))
print("Factorial Of Number is :",fact(n))