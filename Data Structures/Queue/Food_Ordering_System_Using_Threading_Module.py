from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,data):
        self.buffer.appendleft(data)
    def dequeue(self):
        return self.buffer.pop()

    def place_order(self,orders):
        for order in orders:
            self.enqueue(order)
            print("Order is Placed for",order)
            time.sleep(0.5)
        
    def server_order(self):
        time.sleep(1)
        while len(self.buffer) != 0:
            print("Order for",self.dequeue(),"is Served")
            time.sleep(2)
        
if __name__ == "__main__":
    fos = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
    
    t1 = threading.Thread(target=fos.place_order(orders))
    t2 = threading.Thread(target=fos.server_order())
    
    t1.start()
    t2.start()