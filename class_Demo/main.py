class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print(self.cpu,self.ram)

comp1= Computer('i5',16)
comp2 = Computer('i7',24)

comp1.config()
comp2.config()

