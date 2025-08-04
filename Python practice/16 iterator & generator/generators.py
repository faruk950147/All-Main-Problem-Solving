# generator is an object that can be iterated (one by one)
import time

# generator function
# def gen():
#     yield "Hello"
#     time.sleep(1)
#     yield "World"
#     time.sleep(1)
#     yield "Generator"

# # generator object
# g = gen()
# print(next(g))
# time.sleep(1)
# print(next(g))
# time.sleep(1)
# print(next(g))

def countdown(num):
    print("Countdown started")
    while num > 0:
        yield num
        num -= 1
    print("Countdown finished")

for i in countdown(10):
    print(i)


