

def calculate_happiness(n, m, arr, A, B):
    A = set(A)
    B = set(B)
    happiness = 0
    for num in arr:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1
    return happiness

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(calculate_happiness(n, m, arr, A, B))
