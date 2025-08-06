# given a list find the multiplication table of all elements
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in li:
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}", end='\t')
#     print()

# def MultiplicationTable(li):
#     for i in li:
#         for j in range(1, 11):
#             print(f"{i} * {j} = {i * j}", end='\t')
#         print(end='\n')

# nums = list(map(int, input().split()))
# MultiplicationTable(nums)

# given a number find the multiplication table of that number
def MultiplicationTable(n):

    for i in range (1, 11): 

        # multiples from 1 to 10
        print ("%d * %d = %d" % (n, i, n * i))

if __name__ == "__main__":
  n = int(input())
  MultiplicationTable(n)

# def multiplicationTable(*n):
#     for i in range(1, 11):
#         for j in n:
#             print(f"{j} * {i} = {j * i}", end='\t')
#         print(end='\n')
# multiplicationTable(1, 2, 3)


