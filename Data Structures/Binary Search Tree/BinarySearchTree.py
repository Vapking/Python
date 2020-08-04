class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self,data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
        
    def inorder_traversel(self):
        elements = []
        
        if self.left:
            elements += self.left.inorder_traversel()
            
        elements.append(self.data)
        
        if self.right:
           elements += self.right.inorder_traversel()
        
        return elements 
    
    def preOrder_traversel(self):
        elements = [self.data]
        
        if self.left:
            elements += self.left.preOrder_traversel()
        if self.right:
            elements += self.right.preOrder_traversel()
        
        return elements

    def postOrder_traversel(self):
        elements = []
        if self.left:
            elements += self.left.postOrder_traversel()
        if self.right:
            elements += self.right.postOrder_traversel()
        
        elements.append(self.data)
        
        return elements
    
    def search(self,val):
        
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        elements = self.inorder_traversel()
        return sum(elements)
    
    def rDelete_node(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.rDelete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.rDelete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
        
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.rDelete_node(min_val)
        
        return self

    def lDelete_node(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.lDelete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.lDelete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.lDelete_node(max_val)
        
        return self
    
def build_Binary_Search_Tree(elements):
    print("Building Tree With these Elements : ",elements)
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":

    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_Binary_Search_Tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    # numbers_tree = build_Binary_Search_Tree([17, 4, 1, 20, 9, 23, 18, 34])
    # print("Minimum Node in Tree is :",numbers_tree.find_min())
    # print("Maximum Node in Tree is :",numbers_tree.find_max())
    # print("Sum of all Elements in Tree is :",numbers_tree.calculate_sum())
    # numbers_tree = build_Binary_Search_Tree([15,12,7,14,27,20,23,88 ])
    # print("Tree In In Order Traversel is :",numbers_tree.inorder_traversel())
    # print("Tree In Pre Order Traversel is :",numbers_tree.preOrder_traversel())
    # print("Tree In Post Order Traversel is :",numbers_tree.postOrder_traversel())
    
    # numbers_tree = build_Binary_Search_Tree([17, 4, 1, 20, 9, 23, 18, 34])
    # numbers_tree.rDelete_node(20)
    # print("After deleting 20 ",numbers_tree.inorder_traversel()) # this should print [1, 4, 9, 17, 18, 23, 34]

    # numbers_tree = build_Binary_Search_Tree([17, 4, 1, 20, 9, 23, 18, 34])
    # numbers_tree.rDelete_node(9)
    # print("After deleting 9 ",numbers_tree.inorder_traversel())  # this should print [1, 4, 17, 18, 20, 23, 34]

    # numbers_tree = build_Binary_Search_Tree([17, 4, 1, 20, 9, 23, 18, 34])
    # numbers_tree.rDelete_node(17)
    # print("After deleting 17 ",numbers_tree.inorder_traversel())  # this should print [1, 4, 9, 18, 20, 23, 34]
    
    # numbers_tree = build_Binary_Search_Tree([17, 4, 1, 20, 9, 23, 18, 34])
    # numbers_tree.lDelete_node(20)
    # print("After deleting 20 ",numbers_tree.inorder_traversel()) # this should print [1, 4, 9, 17, 18, 23, 34]

    # numbers_tree = build_Binary_Search_Tree([17, 4, 1, 20, 9, 23, 18, 34])
    # numbers_tree.lDelete_node(9)
    # print("After deleting 9 ",numbers_tree.inorder_traversel())  # this should print [1, 4, 17, 18, 20, 23, 34]

    # numbers_tree = build_Binary_Search_Tree([17, 4, 1, 20, 9, 23, 18, 34])
    # numbers_tree.lDelete_node(17)
    # print("After deleting 17 ",numbers_tree.inorder_traversel())  # this should print [1, 4, 9, 18, 20, 23, 34]
    