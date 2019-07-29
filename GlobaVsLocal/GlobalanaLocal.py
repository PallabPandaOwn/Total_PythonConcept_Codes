

a =10 #global variable

# def fun():
#
#     global a
#     a=15
#     b=10
#     print(a)
#
# fun()
# print(a)


c=10
def fun1():
    c=15
    x = globals()['c'] # getting global variable
    print(c)
    print(x)
    globals()['c'] = 20
    x = globals()['c']  # getting global variable
    print(x)

fun1()
