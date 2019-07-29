
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(10):
            sleep(2)
            print("Hello")


class Hi(Thread):
    def run(self):
        for i in range(10):
            sleep(2)
            print("Hi")

t1 = Hello()
t2 = Hi()

t1.start()
sleep(1)
t2.start()