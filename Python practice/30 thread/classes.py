import threading
import time

# create a thread class inherit from threading.Thread
class Thread(threading.Thread):
    def run(self):
        for i in range(3):
            print(threading.current_thread().name)
            print(f"Thread Running: {i}")
            time.sleep(1)

t = Thread()
t.start()
t.join()

# create a thread class inherit from threading.Thread

class Example(threading.Thread):
    # display method as run method
    def display(self):
        for i in range(3):
            print(threading.current_thread().name)
            print(f"Thread Running: {i}")
            time.sleep(1)

exp = Example()
t1 = threading.Thread(target=exp.display)
t1.start()
t1.join()
