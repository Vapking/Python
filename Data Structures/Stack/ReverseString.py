class Stack:
    def __init__(self,MAX):
        self.MAX = MAX
        self.arr = [None for i in range(self.MAX)]
        self.top = -1
        
    def Push(self,char):
        self.top += 1
        self.arr[self.top] = str(char)
    
    def Pop(self):
        char = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return char

def main():
    string = "We will conquere COVID-19"
    s = Stack(len(string))
    for char in string:
        s.Push(char)
    revString = ""
    for i in range(len(s.arr)):
        revString += str(s.Pop())
    print("Reversed String is : ", revString)

if __name__ == "__main__":
    main()