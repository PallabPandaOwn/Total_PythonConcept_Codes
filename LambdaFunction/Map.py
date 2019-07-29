


nums = range(12,45)
evens = filter(lambda n:n%2==0,nums)


double = map(lambda n:int(n/2),evens)


print(type(evens))

print(type(double))

# for i in evens:
#     print(i)


for i in double:
    print(i)
