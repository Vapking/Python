def fib():
    n = int(input("Enter Number for Fibonacci Series :"))
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n<0:
        print("Enter Number greater then Zero!")
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c,end=" ")

def fact():
    n = int(input("Enter Number to get Factorial of :"))
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print("Factorial is =",fact)

def PalidromeString():
    str = input("Enter A String :")
    str1 = str[::-1]
    if str == str1:
        print("Entered String is Palidrome !")
    else :
        print("String is not Palidrome !")

def PalidromeInteger():
    n = int(input("Enter A Number :"))
    tmp = n
    rev = 0
    while(n>0):
        dig = n%10
        rev = rev*10+dig
        n = n/10
    if tmp == rev:
        print("Entered Number is Plidrome !")
    else:
        print("Number is Not Palidrome !")


print("Welcome")
while True:
    print("\n====================Menu====================")
    print("1.Fibbonacci Series")
    print("2.Factorial of Number")
    print("3.Palidrome String or not")
    print("4.Palidrome Number or not")

    ch = int(input("Enter Choice :"))

    if ch==1:
        fib()
    elif ch==2:
        fact()
    elif ch==3:
        PalidromeString()
    elif ch==4:
        PalidromeInteger()
    else:
        print("Thank you")
        break