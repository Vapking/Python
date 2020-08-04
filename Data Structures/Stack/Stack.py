class Stack:
    def __init__(self,MAX):
        self.MAX = MAX
        self.arr = [None for i in range(self.MAX)]
        self.top = -1
        
    def Push(self):
        if self.top == self.MAX-1:
            print("Stack is Full!")
        else:
            self.top += 1
            self.arr[self.top] = int(input("Enter Element in Stack :"))
            print(self.top)
    
    def Pop(self):
        if self.top == -1:
            print("Stack is Empty!")
        else:
            print(self.arr[self.top],"Elements is Poped from Stack.")
            self.arr[self.top] = None
            self.top -= 1
    
    def Peek(self):
        if self.top == -1:
            print("Stack is Empty!")
        else:
            return self.arr[self.top]
        
def main():
    
    s = Stack(int(input("Enter Size of Stack : ")))
    
    while True:
        print("**** Menu ****")
        print("1. Push a Element in Stack.")
        print("2. Pop a Element from Stack.")
        print("3. Peek the Top Element in Stack")
        print("4. Display Stack")
        print("5. Exit")
        
        ch = int(input("Enter your Choice : "))
        
        if ch == 1:
            s.Push()
        elif ch == 2:
            s.Pop()
        elif ch == 3:
            print("Top Element in Stack : ",s.Peek())
        elif ch == 4:
            print(s.arr)
        elif ch == 5:
            print("Bye Bye !")
            break
    
if __name__ == "__main__":
    main()