#method work
# start() # start the thread
# run() # run the thread
# join() # wait for the thread to finish

import threading
import time

def task():
    print("Task started")
    time.sleep(2)
    print("Task finished")
def task2():
    print("Task2 started")
    time.sleep(2)
    print("Task2 finished")

thread = threading.Thread(target=task)
thread2 = threading.Thread(target=task2)
thread.start()
thread.join()
thread2.start()
thread2.join()
print("Main thread finished")


