N = int(input())
A = list(map(int,input().split()))

from itertools import permutations

result = 0
for p in permutations(A):
    temp = 0

    for i in range(N-1):
        temp += abs(p[i]-p[i-1])

    result = max(result, temp)

print(result)
