# def find_max(*nums):
#     return max(nums)
# print(find_max(1, 2, 3, 4, 5))

def find_max(*nums):
    max_num = nums[0]
    # for num in range(len(nums)):
    #     if nums[num] > max_num:
    #         max_num = nums[num]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


print(find_max(1, 2, 3, 4, 5))
