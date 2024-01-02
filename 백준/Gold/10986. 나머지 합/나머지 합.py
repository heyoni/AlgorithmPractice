n, m = map(int, input().split())
k = list(map(int, input().split()))
answer = 0
s = [0]*n
c = [0]*m
for i in range(n):
    if i == 0:
        s[0] = k[0]
    else:
        s[i] = s[i-1] + k[i]


for i in range(n):
    remainder = s[i] % m
    if remainder == 0:
        answer += 1
    c[remainder] += 1

for i in range(m):
    if c[i] > 1:
        answer += (c[i]*(c[i]-1) // 2)

print(answer)