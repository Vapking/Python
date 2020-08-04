from collections import deque
import time

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,data):
        self.buffer.appendleft(data)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)

    def place_order(self,data):
        self.enqueue(data)
        print("Order is Placed For",data)
    def server_order(self):
        print("Order For",self.dequeue(),"is Severed!")
        
if __name__ == "__main__":
    fos = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
    for order in orders:
        time.sleep(0.5)
        fos.place_order(order)
        time.sleep(2)
        fos.server_order()