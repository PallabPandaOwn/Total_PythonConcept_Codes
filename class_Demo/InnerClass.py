class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.innerClass()

    def show(self):
        print(self.name, self.rollno)
        # print(self.lap.brand)


    class innerClass:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram =16
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = Student('pallab',1)
s2 = Student('Ravi',2)

s1.show()
s2.show()
s1.lap.show()

s3 = Student.innerClass()
print(type(s3))
s3.show()

