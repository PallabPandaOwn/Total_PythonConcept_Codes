


nums = range(12,45)
evens = filter(lambda n:n%2!=0,nums)

print(type(evens))

for i in evens:
    print(i)

