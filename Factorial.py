x = int(input("Enter a number:"))


# Simple way
def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    print(f)

fact(x)


# using recursion

def fact_1(n):
    f=0
    if n == 0:
        return 1
    else:
        f=n * fact_1(n - 1)
        return f


print(fact_1(x))
