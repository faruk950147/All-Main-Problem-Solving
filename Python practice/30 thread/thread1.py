# A process is a heavy-weight execution unit that contains its own memory space.
# A thread is a light-weight sub-process (a part of a process) and shares memory with other threads of the same process.

# A thread is a sequence of executable instructions within a process.
# Threads run concurrently and share resources (like memory) with other threads in the same process.

# Threads in Python can be created using the 'threading' module.

# In Python, a thread is an object of the 'Thread' class (threading.Thread).
# 1. User Thread (User Thread)
# 2. Daemon Thread (Daemon Thread)
# 3. Single Thread (Single Thread)  
# 4. Multi Thread (Multi Thread) 
# 5. Thread Synchronization (Thread Synchronization)


# 1. User Thread (User Thread)
# A user thread is a thread that is created by the user (programmer) and is used to perform specific tasks.
# User threads are also known as application threads or foreground threads.
# User threads are used to perform tasks such as file I/O, network I/O, and other I/O operations.
# User threads are used to perform tasks such as file I/O, network I/O, and other I/O operations.

# 2. Daemon Thread (Daemon Thread)
# A daemon thread is a thread that is created by the system and is used to perform background tasks.
# Daemon threads are also known as system threads or background threads.
# Daemon threads are used to perform tasks such as garbage collection, memory management, and other system-level tasks.
# Daemon threads are used to perform tasks such as garbage collection, memory management, and other system-level tasks.

# 3. Single Thread (Single Thread)
# A single thread is a thread that is created by the user (programmer) and is used to perform specific tasks.
# Single threads are also known as application threads or foreground threads.
# Single threads are used to perform tasks such as file I/O, network I/O, and other I/O operations.
# Single threads are used to perform tasks such as file I/O, network I/O, and other I/O operations.

# 4. Multi Thread (Multi Thread)
# A multi thread is a thread that is created by the user (programmer) and is used to perform specific tasks.
# Multi threads are also known as application threads or foreground threads.
# Multi threads are used to perform tasks such as file I/O, network I/O, and other I/O operations.
# Multi threads are used to perform tasks such as file I/O, network I/O, and other I/O operations.

# 5. Thread Synchronization (Thread Synchronization)
# Thread synchronization is a technique used to control access to shared resources in a multi-threaded environment.
# Thread synchronization is used to prevent race conditions and ensure data consistency.
# Thread synchronization is used to prevent race conditions and ensure data consistency.
# all attributes of thread
# name
# is_alive
# daemon
# ident
# isDaemon

# methods
# getName
# setName
# run
# start
# join
import threading

# print(threading.current_thread().name)
# print(threading.current_thread().is_alive())
# print(threading.current_thread().daemon)
# print(threading.current_thread().ident)
# print(threading.current_thread().getName())
# print(threading.current_thread().setName("MyThread"))
# print(threading.current_thread().run())
# print(threading.current_thread().start())
# print(threading.current_thread().join())

def display(n):
    for i in range(10):
        print(n)
        
thread1 = threading.Thread(target=display, args=("Hello",)) #(5,"Hello")
thread2 = threading.Thread(target=display, args=("World",)) #(5,"World")

thread1.start()
thread2.start()

# def display(n, msg):
#     for i in range(10):
#         print(n, msg)
        
# thread1 = threading.Thread(target=display, args=("Hello", "Welcome"))
# thread2 = threading.Thread(target=display, args=("World", "Welcome"))
# t3 = threading.Thread(target=display, kwargs={"n": "Python"})
# t4 = threading.Thread(target=display, kwargs={"n": "Thread"})

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()
