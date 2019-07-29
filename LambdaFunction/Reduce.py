

from functools import reduce


nums = range(12,45)
evens = filter(lambda n:n%2==0,nums)


double = map(lambda n:int(n/2),evens)


Reduce = reduce(lambda n,m:n+m,double)

# print(type(evens))
#
# print(type(double))

print(type(Reduce))
print(Reduce)
# for i in evens:
#     print(i)

