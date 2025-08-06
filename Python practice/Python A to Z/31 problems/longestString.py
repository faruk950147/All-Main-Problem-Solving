# def longestString(arr):
#     max = 0
#     for i in arr:
#         if len(i) > max:
#             max = len(i)
#     return max
def longestString(arr):
    max = 0
    for i in range(len(arr)):
        if len(arr[i]) > max:
            max = len(arr[i])
    return [max, arr[i]]
print(longestString(["Hello", "World", "Python", "Programming"]))

def longestString2(arr):
    longestString = ""
    for i in range(len(arr)):
        if len(arr[i]) > len(longestString):
            longestString = arr[i]
    return [longestString, len(longestString)]

print(longestString2(["Hello", "World", "Python", "Programming"]))