from numpy import *

lst = arange(0,5)
print(lst)


def BSearch(lst, n):
    l = 0
    u = len(lst) - 1
    mid = (l + u) // 2
    print(mid)
    for i in lst:
        if i == n:
            return True
        else:
            if i < n:
                l = mid
            else:
                u = mid
    else:
        return False


if BSearch(lst, 19):
    print("Found")
else:
    print("Not found")
