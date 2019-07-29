class Test:
    def func(self):
        print("hello")

    def divide(self):
        x = 2 / 0;

    def __del__(self):
        pass

    def __str__(self):
        return "This is Test class"


t = Test()
print(t)

# magic function or Dunder fuction
