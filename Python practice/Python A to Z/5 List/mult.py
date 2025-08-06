

li = [1,2,3,4,5,6,7,8,9,10]
li1 = [2,3,4]
l2 = []
total = 0
sum1 = 0

# for i in li:
#     total *= i
# print(total)

for i in range(len(li1)):
    total *= li1[i]
    sum1 += li1[i]*li1[i]
    l2.append(total)
    l2.append(sum1)

print(total)
print(sum1)
print(l2)

# for i in li1:
#     total += i*i
#     l2.append(i*i)
# print("total",total)
# print("l2",l2)

# for i in range(len(li1)):
#     total += li1[i]*li1[i]
#     l2.append(li1[i]*li1[i])
# print("total",total)
# print("l2",l2)