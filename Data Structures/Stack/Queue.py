class Queue:
    def __init__(self,size):
        self.MAX = size
        self.arr = [None for i in range(self.MAX)]
        self.front = self.rear = -1
    
    def Enqueue(self):
        if self.rear == self.MAX-1:
            print("Queue is Full!")
        elif self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.arr[self.rear] = input("Enter Data in Queue :")
        else:
            self.rear += 1
            self.arr[self.rear] = input("Enter Data in Queue :")
            print("Front : ",self.front)
    
    def Dequeue(self):
        if self.front == -1:
            print("Queue is Empty!")
        elif self.front >= self.rear:
            if self.arr[self.rear] is not None:
                self.arr[self.front] = None
                self.front = self.rear = -1
            else:
                print("Queue is Empty!")
        else:
            print("Front : ",self.front)
            self.arr[self.front] = None
            self.front += 1
            
def main():
    
    Q = Queue(int(input("Enter Size of Queue : ")))
    
    while True:
        print("**** Menu ****")
        print("1. Insert a Element in Queue.")
        print("2. Delete a Element in Queue.")
        print("3. Display Queue")
        print("4. Exit")
        
        ch = int(input("Enter your Choice : "))
        
        if ch == 1:
            Q.Enqueue()
        elif ch == 2:
            Q.Dequeue()
        elif ch == 3:
            print(Q.arr)
        elif ch == 4:
            print("Bye Bye !")
            break

if __name__ == "__main__":
    main()
            