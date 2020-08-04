class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        hash = 0 
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for elements in self.arr[h]:
            if elements[0] == key:
                return elements[1]
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx, elements in enumerate(self.arr[h]):
            if len(elements)==2 and elements[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

if __name__  == "__main__":
    t = HashTable()
    t['march 6'] = 130
    t['jan 2'] = 70
    t['dec 17'] = 110
    t['march 17'] = 465
    print(t.arr)