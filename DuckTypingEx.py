class PyCharm :
	
	def execute(self):
		print("Compiling......")
		print("Running......")

class MyEditor :
	
	def execute(self):
		print("Spell Checking....")
		print("Convention Checking....")
		print("Compiling......")
		print("Running......")	

class Laptop :
	
	def __init__(self,ide):
		ide.execute()

ide = MyEditor()

lap1 = Laptop(ide)