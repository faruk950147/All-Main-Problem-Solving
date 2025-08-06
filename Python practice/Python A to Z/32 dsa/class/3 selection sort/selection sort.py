class SelectionSort:
    def __init__(self):
        pass
    def selection_sort(self, lst):
        for i in range(len(lst)):
            min_idx = i
            for j in range(i + 1, len(lst)):
                if lst[j] < lst[min_idx]:
                    min_idx = j
            if min_idx != i:
                lst[i], lst[min_idx] = lst[min_idx], lst[i]
        return lst
    
if __name__ == "__main__":
    lst = [5, 2, 3, 1, 4]
    print("Before sorting:", lst)
    selection_sort = SelectionSort()
    print("After sorting:", selection_sort.selection_sort(lst))