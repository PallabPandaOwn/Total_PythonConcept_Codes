


a=4
b='r'

try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("Somthing wrong..")