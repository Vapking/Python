class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
    
    def insert_at_beg(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
    
    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        llstr += "None"
        print(llstr)
    
    def insert_at_end(self,data):
        if self.head is None:
            newNode = Node(data,None)
            self.head = newNode
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)
        
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if index == 0:
            self.insert_at_beg(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
            itr = itr.next
            count += 1
    
    def insert_after_value(self,data_after,data_insert):
        count = 0
        flag = False
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(count+1,data_insert)
                flag = True
                break
            itr = itr.next
            count += 1
        
        if flag:
            pass
        else:
            raise Exception("Invalid Data")
    
    def remove_by_value(self,data):
        count = 0
        flag = False
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(count)
                flag = True
                break
            itr = itr.next
            count += 1
        
        if flag:
            pass
        else:
            raise Exception("Invalid Data")
    
    def remDuplicates(self):
        itr1 = self.head
        itr2 = self.head.next
        while itr1.next:
            if itr1.data == itr2.data:
                itr1.next = itr1.next.next
            itr1 = itr1.next
            itr2 = itr2.next
            
if __name__ == "__main__":
    n = int(input())
    ll = Linked_List()
    for i in range(n):
        ll.insert_at_end(input())
    ll.print()
    ll.remDuplicates()
    ll.print()
    