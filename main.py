import time
from machine import Pin



przycisk = Pin(0, Pin.IN, Pin.PULL_UP)

def manual():
    while True:
        time.sleep(10)
        print("przycisk")
        print(przycisk.value())


def auto():
    pass


print("Wcisnij przycisk")
manual()
