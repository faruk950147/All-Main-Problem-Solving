# When a variable is passed to a function, its reference (actual address) is sent.
# As a result, any changes made inside the function also affect the original variable outside.
# যখন ভ্যারিয়েবল function-এ পাঠানো হয় তার রেফারেন্স (মূল address) পাঠানো হয়।

# ফলে function এর ভেতর যা পরিবর্তন হয়, তা বাইরে মূল ভ্যারিয়েবলেও প্রভাব ফেলে।

def pass_by_reference(x):
    print(f"{x} Before memory location inside function:", x, id(x))
    x[0] = 20
    print(f"{x} Inside function x:", x)
    print(f"{x} After memory location inside function x:", x, id(x))
    return x

x = [10]  # mutable object (list)
print(f"{x} Before modification x:", x, id(x))
pass_by_reference(x)
print(f"{x} After modification x:", x, id(x))

# def pass_by_reference(lst):
#     print(f"{lst} Before memory location inside function:", lst, id(lst))
#     lst[0] = lst[0] + 1
#     # lst[0] += 1 # pass by reference    
#     print(f"{lst} Inside function lst:", lst)
#     print(f"{lst} After memory location inside function lst:", lst, id(lst))
#     return lst


# li = [10]
# print(f"{li} Before modification li:", li, id(li))
# pass_by_reference(li)
# print(f"{li} After modification li:", li, id(li))


# def change_list(lst):
#     print(f"{lst} before memory location inside function:", lst, id(lst))   
#     lst.append(100)
#     print(f"{lst} Inside function lst:", lst)
#     print(f"{lst} after memory location inside function lst:", lst, id(lst))
#     return lst

# list1 = [1, 2, 3]
# print(f"{list1} Before modification list1:", list1, id(list1))
# change_list(list1)
# print(f"{list1} After modification list1:", list1, id(list1))  # Output: [1, 2, 3, 100]


