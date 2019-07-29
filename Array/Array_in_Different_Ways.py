'''
In Numpay there are 6 ways to create array
1.Array()
2.Linespace()
3.Logspace()
4.arange()
5.Zeros()
6.Ones()
'''

from numpy import *


arr = array([1,2,3,4])
print(arr)

arr2 = linspace(0,20)
print('%2.f'%arr2[0])

arr3 = logspace(0,20,5)
print(arr3)

arr3 = zeros(5)
print(arr3)

arr4 = ones(3)
print(arr4)