from socket import *
check = input("Do You Want IP Address : ")
if check == 'n' or check =='N':
    exit()
else:
    print("Your Computer IP Address is : ",gethostbyname(gethostname()))