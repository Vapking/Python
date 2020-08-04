class  TreeNode:
    
    def __init__(self,data):
        self.data = data
        self.childern = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.childern.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
            
        return level
    
    def print_tree(self):
        spaces = " " * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + self.data)
        if self.childern:
          for child in self.childern:
              child.print_tree()  

def produce_tree():
    root = TreeNode("Electronics")
    
    laptops = TreeNode("Laptops")
    laptops.add_child(TreeNode("Dell"))
    laptops.add_child(TreeNode("HP"))
    laptops.add_child(TreeNode("Asus"))
    
    cell_phones = TreeNode("Cell Phones")
    cell_phones.add_child(TreeNode("IPhone"))
    cell_phones.add_child(TreeNode("Samsung"))
    cell_phones.add_child(TreeNode("Vivo"))
    
    tv = TreeNode("Tv")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    
    root.add_child(laptops)
    root.add_child(cell_phones)
    root.add_child(tv)
    
    return root
    
if __name__ == "__main__":
    root = produce_tree()
    root.print_tree()