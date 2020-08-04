from time import sleep
from threading import *

class Even(Thread):
	def run(self):
		for i in range(2,11,2):
			print(i)
			sleep(1)

class Odd(Thread):
	def run(self):
		for i in range(1,11,2):
			print(i)
			sleep(1)


e = Even()
o = Odd()

o.start()
e.start()
