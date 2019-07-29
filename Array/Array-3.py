# create an array with 5  element and delete the value at index 2

import array as Array

arr = Array.array('i', [])

arr_size = int(input("Enter the size of an array :- "))

for i in range(arr_size):
    value = int(input("Enter the elements :- "))
    arr.append(value)

print("Elements inside an array are {}".format(arr))

print("\n")
del_val = int(input("Enter the index number to delete the value :-"))

k =0

for e in arr:
    if del_val==k:
        arr.pop(k)
        k+=1
print(arr)

