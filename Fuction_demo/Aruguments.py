'''
*args vs **kwargs
'''

def Test(b, **a):
    # c = b+a
    print(type(a))


Test(2,a = 28)

#c = {1:12}
