def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

nitem = int(input("Enter till how Many Number You Want Fibonacci Series :"))

if nitem <= 0:
    print("Enter A Number Greater Then Zero")
else:
    print("Fibonacci Series is :")
    for i in range(nitem):
        print(Fibonacci(i))
