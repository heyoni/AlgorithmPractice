input()
scores = list(map(int,input().split()))

max_score = max(scores)
sum_score = sum(scores)

print(sum_score/max_score*100/len(scores))