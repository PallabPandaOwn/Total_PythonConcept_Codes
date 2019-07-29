from numpy.ma import arange

lst = [23, 12, 1, 45, 67, 45]


def BSort(lst):
    for i in range(0, len(lst)-1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

BSort(lst)
print(lst)
