import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = list(map(int, input().split()))
s = [0]*n
for i in range(n):
    if i ==0:
        s[i] = k[i]
    s[i] = s[i-1] + k[i]
for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        print(s[b-1])
    else:
        print(s[b-1]-s[a-2])