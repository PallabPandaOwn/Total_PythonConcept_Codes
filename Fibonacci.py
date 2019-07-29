x = int(input("Enter a number:"))


def fibo(n):
    a = 0
    b = 1
    if n < 0:
        print('incorrect number')
    elif n == 0:
        print(n)
    elif n == 1:
        print(n)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            # print(c)
            if c >100:
                break
        print(a)



fibo(x)
