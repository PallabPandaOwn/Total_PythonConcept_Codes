class Computer():
    classinfo = "test class"
    def __init__(self):
        self.name = 'Pallab'
        self.age = 30

    def compare(self, others):
        if c1.age == c2.age:
            print("Age are same")
        else:
            print("Age are different")
    @classmethod
    def getClassInfo(cls):
        print(cls.classinfo)
    @staticmethod
    def getinfo():
        print("This is a test programe for static method.")

c1 = Computer()
c1.age = 32
c2 = Computer()
c2.age = 32

print(id(c1))
print(id(c2))

print(c1.name)
print(c2.age)

c1.compare(c2)

Computer.getClassInfo()
Computer.getinfo()
