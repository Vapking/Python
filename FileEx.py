f = open("SoftClone.jpg","rb")

f1 = open("Co.jpg","wb")

for i in f:
	f1.write(i)

f.close()
f1.close()