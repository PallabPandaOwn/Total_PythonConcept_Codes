class A:
    def __init__(self):
        print("A")

    def feature1(self):
        print("Working 1")

    def feature2(self):
        print("Working 2")


class B(A):
    def feature3(self):
        print("Working 3")

    def feature4(self):
        print("Working 4")


a = A()
a = B()
