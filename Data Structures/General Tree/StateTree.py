class TreeNode:
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
    
    def print_tree(self,level):
        spaces = " " * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + self.data)
        if self.childern:
                for child in self.childern:
                    if child.get_level() <= level:
                        child.print_tree(level)

def build_state_tree():
    root = TreeNode("Global")
    
    india = TreeNode("India")
    
    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahamdabad"))
    gujarat.add_child(TreeNode("Baroda"))
    
    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))
    
    india.add_child(gujarat)
    india.add_child(karnataka)
    
    usa = TreeNode("USA")
    
    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))
    
    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))
    
    usa.add_child(new_jersey)
    usa.add_child(california)
    
    root.add_child(india)
    root.add_child(usa)
    
    return root


if __name__ == "__main__":
    root = build_state_tree()
    root.print_tree(1)
    print()
    root.print_tree(2)
    print()
    root.print_tree(3)