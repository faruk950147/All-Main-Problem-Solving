class Search:
    def __init__(self):
        pass
    def linear_search(self, lst, target):
        for i in range(len(lst)):
            if lst[i] == target:
                return i
        return -1

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print("Before search:", lst)
    target = 3
    search = Search()
    print("After search:", search.linear_search(lst, target))
    
