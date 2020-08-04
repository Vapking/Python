class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            elements = self.arr[prob_index]
            if elements is None:
                return
            if elements[0] == key:
                return elements[1]

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,value)
        else:
            new_h = self.find_slot(key,h)
            self.arr[new_h] = (key,value)
    
    def get_prob_range(self,index):
        return [*range(index,len(self.arr))] + [*range(0,index)]
        
    def find_slot(self,key,index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("HashMap is Full")
        
if __name__ == "__main__":
    try:
        t = HashTable()
        t['march 6'] = 130
        t['march 17'] = 456
        t['march 9'] = 90
        t['dec17'] = 110
        t['may 10'] = 50
        t['jan 1'] = 300
        t['feb 28'] = 200
        t['april 10'] = 150
        t['jun 31'] = 1000
        t['jul 30'] = 250
        print(t.arr)
    except Exception as e:
        print(e)