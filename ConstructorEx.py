class A:
	def __init__(self):
		print("in A Init")

	def feature1(self):
		print("Feature 1 Working")

	def feature2(self):
		print("Feature 2 Working")

class B:	
	def __init__(self):
		print("in B Init")

	def feature3(self):
		print("Feature 3 Working")

class C(A,B):
	def __init__(self):
		super().__init__()
		print("in C Init")

	def feature5(self):
		print("Feature 5 Working")

c1 = C()