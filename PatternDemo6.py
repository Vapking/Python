# A P Q R
# A B Q R
# A B C R
# A B C D

no1 = 65
no2 = 80
for i in range(1,5):
    for j in range(i): 
        print(chr(no1+j),"",end="")
    for k in range(4-i):
        print(chr(no2+k),"",end="")
    print()
    no2+=1
