import time
# # for i in range(10):
# #     print(f"Hello World {i}")
    
# # range(start, stop, step) range is iterable object 
# for i in range(1, 11, 2): # range(start, stop, step) range(start, stop) range(stop)bydefault start is 0 by default increase step is 1 and decrease step is -1
#     print(f"{i}")
    
# for i in range(10, 0, -1): # range(start, stop, step) range(start, stop) range(stop)bydefault start is 0 by default increase step is 1 and decrease step is -1
#     print(f"{i}")
    

# for i in range(1, 11): # range(start, stop, step) range(start, stop) range(stop)bydefault start is 0 by default increase step is 1 and decrease step is -1
#     print(f"{i}")

# it iterable object 
# li = [1,2,3,4,5,6,7,8,9,10]
# # for loop in iterable object 
# for i in li:
#     print(f"{i}")

# # it iterable object 
# for i in range(len(li)):
#     print(f"{li[i]}")
    
# tup = (1,2,3,4,5,6,7,8,9,10)
# for i in range(len(tup)):
#     print(f"{tup[i]}")
    


# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# for key in dict1.keys():
#     print(key)
# for key in dict.fromkeys(['a', 'b', 'c']): # dict is a constructor function in class dict
#     # dict.fromkeys(['a', 'b', 'c']) create a dictionary with keys 'a', 'b', 'c' and values None
#     print(key)

# # %timeit [i**2 for i in range(1000000)] # just for comparison notebook


start = time.time()
[i**2 for i in range(1000000)]
end = time.time()

print("Time taken:", end - start, "seconds")

for key in dict.fromkeys(['a', 'b', 'c']):
    print(key)
