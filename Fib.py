n = int(input("Enter Number for Fibbonacci Series :"))
a = 0
b = 1
if n == 1:  
    print(a)
elif n<=0:
    print("Enter Number Greater then Zero !")
else:
    print(a)
    print(b)
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)