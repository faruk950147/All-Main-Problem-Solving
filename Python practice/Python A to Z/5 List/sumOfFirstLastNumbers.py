li = [1,2,3,4,5]
# print(li[0] + li[-1])
# for i in range(len(li)):
#     sum = li[i] + li[-i-1]
# print(sum)

for i in range(int(len(li)/2)):
    sum = li[i] + li[len(li)-i-1] # li[0] + li[4] = 1 + 5 = 6
print(sum)

