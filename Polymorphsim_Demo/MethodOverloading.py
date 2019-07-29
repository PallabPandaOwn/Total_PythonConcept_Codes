class tst:

    def abc(self):
        return 'Hello'

    def abc(self,a=None):
        return a

t = tst()

print(t.abc())
print(t.abc(5))