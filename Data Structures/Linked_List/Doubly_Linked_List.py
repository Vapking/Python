class Node:
	def __init__(self,data=None,next=None,prev=None):
		self.data = data
		self.next = next
		self.prev = prev

class Doubly_Linked_List:
	def __init__(self):
		self.head = self.tail = None
		
	def insert_at_beg(self,data):
		if self.head is None:
			newNode = Node(data,None,None)
			self.head = newNode
		else:
			newNode = Node(data,self.head,None)
			self.head = newNode
	
	def insert_at_end(self,data):
		if self.head is None:
			self.insert_at_beg(data)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		newNode = Node(data,None,itr)
		itr.next = newNode

	def print(self):
		if self.head is None:
			print("List is Empty!")
			return
		itr = self.head
		dllstr = "None <==> "
		while itr:
			dllstr += str(itr.data) + " <==> "
			itr = itr.next
		print(dllstr,"None",sep="")

	def revPrint(self):
		itr = self.head
		while itr.next:
			itr = itr.next
			self.tail = itr
		itr = self.tail
		revstr = "None <==> "
		while itr:
			revstr += str(itr.data) + " <==> "
			itr = itr.prev
		print(revstr,"None",sep="")
	
	def insert_values(self,data_list):
		self.head = self.tail = None
		for data in data_list:
			self.insert_at_end(data)
	
	def get_length(self):
		if self.head is None:
			return 0
		count = 0
		itr = self.head
		while itr:
			count += 1
			itr = itr.next
		return count
		
	def insert_at(self,index,data):
		if index<0 or index>=self.get_length():
			raise Exception("IndexError : Invalid Index")
		if index == 0:
			self.insert_at_beg(data)
		count = 0
		itr = self.head
		while itr:
			if count == index-1:
				newNode = Node(data,itr.next,itr)
				itr.next.prev = newNode		
				itr.next = newNode
				break
			itr = itr.next
			count += 1
	
	def remove_at(self,index):
		if index<0 or index>=self.get_length():
			raise Exception("IndexError : Invalid Index")
		if index == 0:
			self.head = self.head.next
		count = 0
		itr = self.head
		while itr:
			if count == index-1:
				itr.next.next.prev = itr
				itr.next = itr.next.next
				break
			itr = itr.next 
			count += 1
	
	def insert_after_value(self,data_after,insert_data):
		count = 0
		flag = False
		itr = self.head
		while itr:
			if itr.data == data_after:
				self.insert_at(count+1,insert_data)
				flag = True
				break
			itr = itr.next
			count += 1
		if not flag:
			raise Exception("DataError : Invalid Data!")
	
	def remove_after_value(self,data_after):
		count = 0
		flag = False
		itr = self.head
		while itr:
			if itr.data == data_after:
				self.remove_at(count+1)
				flag = True
				break
			itr = itr.next
			count += 1
		if not flag:
			raise Exception("DataError : Invalid Data!")


if __name__ == "__main__":
	dll = Doubly_Linked_List()
	dll.insert_values([10,12,14,16,20])
	dll.print()
	dll.insert_after_value(12,13)
	dll.print()
	dll.remove_after_value(12)
	dll.print()