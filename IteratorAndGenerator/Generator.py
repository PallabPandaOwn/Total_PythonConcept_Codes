

def Topten():

    yield [1,2,3]

val=Topten()

for i in val.__next__():
    print(i)