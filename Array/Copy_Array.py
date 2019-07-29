

from numpy import *


arr = array([1,2,3,4])
# arr1 = array([5,6,7,8])

#first approch
arr1 = arr

#2nd approch

arr1 = arr.view() # Shallow copy

#3rd approch

arr1 = arr.copy() # deep copy


print(arr)