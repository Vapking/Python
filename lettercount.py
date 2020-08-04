str = input("Enter a String :")
ws = 0
count = len(str)
for i in str:
        if i==' ':
                ws = ws+1

letter_count = count-ws

print("Number of letters in String is :",letter_count)
