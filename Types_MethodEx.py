class Student:
	
	school = "Sanjeevan"

	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		return (self.m1+self.m2+self.m3)/3

	def get_marks(self):
		return self.m1,self.m2,self.m3

	def set_marks(self,m1_value,m2_value,m3_value):
		self.m1 = m1_value,self.m2 = m2_value,self.m3 = m3_value
	
	@classmethod
	def getSchool(cls):
		return cls.school

	@staticmethod
	def info():
		print("This is Student Class....")


s1 = Student(34,47,32)
s2 = Student(89,32,12)

print("Marks of M1,M2,M3 : ",s1.get_marks())
print("Avgerage of Marks : ",s2.avg())
print(Student.getSchool())
Student.info()