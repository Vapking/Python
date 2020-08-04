class TopTen :
	
	def __init__(self):
		self.nums = 1

	def __iter__(self):
		return self

	def __next__(self):

		if self.nums <= 10 :
			val = self.nums
			self.nums += 1
			return val
		else :
			raise StopIteration
		
	
values = TopTen()

for i in values :
	print(i)