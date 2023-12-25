import sys
input = sys.stdin.readline

N, M = map(int,input().split())
l = []
condition = []
sum_list = [[0 for _ in range(N + 1)] for _ in range(N + 1)]


for _ in range(N):
    temp = list(map(int,input().split()))
    l.append(temp)


for i in range(1, N+1):
    for j in range(1, N+1):
        sum_list[i][j] = l[i-1][j-1] + sum_list[i][j-1] + sum_list[i-1][j] - sum_list[i-1][j-1]


for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    result = sum_list[x2][y2] - sum_list[x1-1][y2] - sum_list[x2][y1-1] + sum_list[x1-1][y1-1]
    print(result)