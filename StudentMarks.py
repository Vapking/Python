m1,m2,m3 = input("Enter Marks of Three subject : ").split(",")

sum = int(m1)+int(m2)+int(m3)
avg = sum//3
per = (sum*100)//300

print("Sum of Marks :",sum)
print("Average of Marks :",avg)
print("Percentage of Student :",per)

if per>=91:
    print("Distintion")
elif per>=81 and per<=90:
    print("A Grade")
elif per>=71 and per<=80:
    print("B Grade")
elif per>=61 and per<=70:
    print("C Grade")
elif per>=51 and per<=60:
    print("D Grade")
elif per>=40 and per<=50:
    print("E Grade")
else:
    print("Fail")


