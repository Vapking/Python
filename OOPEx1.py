class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Config is {} {}".format(self.cpu,self.ram))


com1 = Computer("i7",16)
com2 = Computer("Ryzen 3",32)

com1.config()
com2.config()