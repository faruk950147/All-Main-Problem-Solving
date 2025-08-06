class Search:
    def __init__(self):
        pass
    def binary_search(self, lst, target):
        left, right = 0, len(lst) - 1
        while left <= right: 
            mid = (left + right) // 2
            if lst[mid] == target:
                return mid
            elif lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print("Before search:", lst)
    target = 3
    search = Search()
    print("After search:", search.binary_search(lst, target))
