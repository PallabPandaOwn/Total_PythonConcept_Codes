

x = [1,2,3,4,5,23,45,67,34,89]


def fun(A_List):
    odd = 0
    even = 0
    for i in A_List:
        if i%2 ==0:
            even += 1
        else:
            odd += 1

    print('Even :{} and odd : {}'.format(even,odd))

fun(x)