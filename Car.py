class Car:
	
	wheels = 4

	def __init__(self):
		self.mil = 10
		self.company = "BMW"

c1 = Car()
c2 = Car()

c2.company = input("Enter company Name :")
c2.mil = int(input("Enter Millage of Car :"))

print("\n Car Company Name : {0} \n Car Millage : {1} \n Car Wheels : {2}".format(c1.company,c1.mil,c1.wheels))
print("\n Car Company Name : {0} \n Car Millage : {1} \n Car Wheels : {2}".format(c2.company,c2.mil,c2.wheels))
