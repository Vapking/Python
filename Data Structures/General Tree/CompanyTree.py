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
    
    def print_tree(self,option="Both"):
        spaces = " " * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        
        if option == "name" or option == "Name":
            print(prefix + self.data[0])
            for child in self.childern:
                child.print_tree(option)
        elif option == "designation" or option == "Designation":
            print(prefix + self.data[1])
            for child in self.childern:
                child.print_tree(option)
        else:
            print(prefix + self.data[0],"(",self.data[1],")")
            for child in self.childern:
                child.print_tree(option)
        
def build_company_tree():
    root = TreeNode(["Nilupul","CEO"])
    
    CTO = TreeNode(["Chinmay","CTO"])
    
    Infra_Head = TreeNode(["Vishwa","Infrastructure Head"])
    Infra_Head.add_child(TreeNode(["Dhaval","Cloud Manager"]))
    Infra_Head.add_child(TreeNode(["Abhijit","App Manager"]))
    
    CTO.add_child(Infra_Head)
    CTO.add_child(TreeNode(["Amir","Application Head"]))
    
    HR = TreeNode(["Gels","HR Head"])
    HR.add_child(TreeNode(["Peter","Recruitment Manager"]))
    HR.add_child(TreeNode(["Waqas","Policy Manager"]))
    
    root.add_child(CTO)
    root.add_child(HR)
    
    return root

if __name__ == "__main__":
    root = build_company_tree()
    root.print_tree("name")
    print()
    root.print_tree("designation")
    print()
    root.print_tree()