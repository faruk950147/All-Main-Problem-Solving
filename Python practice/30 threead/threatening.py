import threading

# current_thread = threading.current_thread().name
# print(current_thread) 

# def display(n):
#     for i in range(10):
#         print(n)
        
# thread1 = threading.Thread(target=display, args=("Hello",))
# thread2 = threading.Thread(target=display, args=("World",))

# thread1.start()
# thread2.start()

def display(n, msg):
    for i in range(10):
        print(n, msg)
        
thread1 = threading.Thread(target=display, args=("Hello", "Welcome"))
thread2 = threading.Thread(target=display, args=("World", "Welcome"))

thread1.start()
thread2.start()
