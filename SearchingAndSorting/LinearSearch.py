'''
Linear search implimetation in python
'''

lst = [12, 34, 56, 23, 1, 7, 8, 5, 4]


def search(list, n):
    for i in lst:
        if i == n:
            return True
    else:
        return False


print(search(lst, 100))
