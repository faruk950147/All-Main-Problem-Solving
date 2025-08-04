def find_fact(li):
    fact_list = []
    for i in li:
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        fact_list.append(fact)
    return fact_list
print(find_fact([2, 3, 4]))



# li = list(map(int, input("Enter a list of numbers: ").split()))
# fact_list = []
# for i in li:
#     fact = 1
#     for j in range(1, i + 1):
#         fact *= j
#     fact_list.append(fact)
# print(fact_list)