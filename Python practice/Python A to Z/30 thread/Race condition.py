import threading
import time

class Bus:
    def __init__(self, name, seat_capacity):
        self.name = name
        self.seat_capacity = seat_capacity
        self.lock = threading.Lock()

    def book_seat(self, need_seat):
        with self.lock:
            print(f"{threading.current_thread().name} is trying to book {need_seat} seats in {self.name}")
            time.sleep(1)
            if self.seat_capacity >= need_seat:
                print(f"{threading.current_thread().name} booked {need_seat} seats in {self.name}")
                self.seat_capacity -= need_seat
            else:
                print(f"{threading.current_thread().name} failed to book {need_seat} seats in {self.name}")

bus1 = Bus("GreenLine", 5)

thread1 = threading.Thread(target=bus1.book_seat, args=(2,), name="Faruk")
thread2 = threading.Thread(target=bus1.book_seat, args=(3,), name="John")

thread1.start()
thread2.start()
thread1.join()
thread2.join()
