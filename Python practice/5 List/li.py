arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

# for i in range(int(len(arr) / 2)):
#     temp = arr[i]
#     arr[i] = arr[len(arr) - 1 - i] #arr[i] = arr[len(arr) - 1] last element assign to first element arr[i] = arr[len(arr) - 1 - i] decrement i value 1
#     arr[len(arr) - 1 - i] = temp #arr[len(arr) - 1 - i] = temp first element assign to last element
# print(arr)

# for i in range(int(len(arr) / 2)):
#     arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    
# print(len(arr)) # print array length
print(arr[len(arr) - 1]) # print last element arr[11] = 110
# print(len(arr) - 1) # print array length arr[11-1] = 10


