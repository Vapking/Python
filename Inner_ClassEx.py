class Student:

	def __init__(self,name,rollno,Laptop):
		self.name = name
		self.rollno = rollno
		self.lap = self.Laptop(brand,cpu,ram)

	def show(self):
		print(self.name,self.rollno)
		self.lap.show()

	class Laptop:

		def __init__(self,brand = 'Dell',cpu = 'i3',ram = 4):
			self.name = brand
			self.cpu = cpu
			self.ram = ram

		def show(self):
			print(self.name,self.cpu,self.ram)


s1 = Student('Omkar',39,('hp','i3','4'))
s2 = Student('Mitesh',14)

s1.show()