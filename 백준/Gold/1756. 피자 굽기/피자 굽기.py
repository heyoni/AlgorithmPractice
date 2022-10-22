D, N = map(int,input().split())
oven = list(map(int, input().split()))
dough = list(map(int,input().split()))

# 1. oven 을 재정렬한다 -> 이전 오븐을 기준으로 그것보다 큰 피자는 들어갈 수 없음
# ex) 5 6 4 3 6 2 3 -> 5 5 4 3 3 2 2
for i in range(len(oven)-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]


# 2. 반죽을 넣는다.
result = 0
oven_idx = len(oven)-1
break_count = 0
for d in dough:
    while oven_idx >= 0:
        if d <= oven[oven_idx]:
            result = oven_idx
            oven_idx -= 1
            break_count += 1
            break
        else:
            oven_idx -= 1


# 실패 -> 첫번째 반죽에서 오븐을 다 돌고 끝난건지, 첫번째 오븐에 있는건지 모름
# if result == 0:
if break_count == len(dough):
    print(result+1)
else:
    print(result)