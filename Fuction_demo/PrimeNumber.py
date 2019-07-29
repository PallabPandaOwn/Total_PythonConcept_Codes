

x = int(input("Eneter a number :"))

def primeCheck(num):
    if num <1:
        print("Incorrect number.")
    else:
        for i in range(2,num):
            if num%i==0:
                print("Not Prime")
                break
        else:
            print("Prime")


primeCheck(x)