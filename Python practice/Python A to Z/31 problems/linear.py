def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return [i, arr[i]]
    return -1

print(linear_search([1, 2, 3, 4, 5], 3))