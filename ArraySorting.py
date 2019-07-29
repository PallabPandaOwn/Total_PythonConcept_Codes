import array as arr

myarr=arr.array('i',[3,1,23,17,90,4,67,89])

def arrsort(x):
    first_num=x[0]
    newarr = arr.array('i',[len(x)])
    for i in x:
        if i <= first_num:
            first_num = i
            newarr.append(first_num)
    #return newarr
    for i in newarr:
        print(i)

arrsort(myarr)
