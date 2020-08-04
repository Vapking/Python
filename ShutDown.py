from os import *
check = input("Do You Want To ShutDown (y/n) : ")
if check == 'n' or check == 'N':
    exit()
else:
    system("shutdown /s /t 10")