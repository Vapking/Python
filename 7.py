def fib():
    n = int(input("Enter Number for Fibonacci Series :"))
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n<0:
        print("Enter Number greater then Zero!")
    else:
        c = a+b
        a = b
        b = c
        print(c)