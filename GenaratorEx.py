def TopTen() :
	n = 1
	while n <= 10 :
		yield n*n 
		n += 1

def Ten() :
	n = 1
	while n <= 10:
		yield n**3
		n += 1 

values = TopTen()
values1 = Ten()

for i in values :
	print(i)

print()

for i in values1 :
	print(i)