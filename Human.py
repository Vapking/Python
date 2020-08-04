class Human:

	def __init__(self):
		self.name = "Vivek"
		self.age = 20

	def compare(self,others):
		if self.age == others.age :
			return True
		else:
			return False

h1 = Human()
h2 = Human()
h2.age = 21

if h1.compare(h2) :
	print("they are same")
else:
	print("they are different")

print(h1.name)
print(h2.name)