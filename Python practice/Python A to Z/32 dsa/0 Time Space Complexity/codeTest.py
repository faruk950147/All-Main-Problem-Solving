# def average(lst):
#     if not lst:
#         return None
#     return sum(lst) / len(lst)
# if __name__ == "__main__":
#     if average([1, 2, 3, 4, 5]) == 3.0:
#         print("Test passed")
#     else:
#         print("Test failed")
    
#     # print(average([1, 2, 3, 4, 5]))
#     # expected_output = 3.0
#     # if expected_output == average([1, 2, 3, 4, 5]):
#     #     print("Test passed")
#     # else:
#     #     print("Test failed")

from re import A


def average(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)

if __name__ == "__main__":
    result = average([1, 2, 3, 4, 5])
    print(f"Average: {result}")
    assert 3.0 == average([1, 2, 3, 4, 5])
    print("Test passed")
    
    # try:
    #     assert result == 3.0
    #     print("Test passed")
    # except AssertionError:
    #     print("Test failed")
