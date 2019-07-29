


#we are dividing 2 numbers .


def div(a,b):
    print(a/b)

#Decoretor

def modify_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner

div = modify_div(div)

div(2,4)