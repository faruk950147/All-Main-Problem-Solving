import threading
import time

class Thread(threading.Thread):
    def run(self):
        for i in range(3):
            print(threading.current_thread().name)
            print(f"Thread Running: {i}")
            time.sleep(1)

t = Thread()
t.start()
t.join()
