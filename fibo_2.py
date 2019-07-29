# Not completed

x = int(input("Enter a number :-"))

def fibo_2(n):
    a=0
    b=1
    if n<0:
        print("incorrect number")
    elif n==0:
        print(n)
    elif n==1:
        print(n)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            print(fibo_2(n-1))
            print(fibo_2(n-2))

fibo_2(x)
