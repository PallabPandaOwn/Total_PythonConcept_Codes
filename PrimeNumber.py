import time


def primeCheck(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


t1 = time.time()
c = 0
for n in range(1, 100000):
    x = primeCheck(n)
    c = c + x
    print("Total :", c)
t2 = time.time()
print(t2 - t2)
# primeCheck(4)
