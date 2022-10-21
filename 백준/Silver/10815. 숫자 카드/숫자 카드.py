N = int(input())
has_card = list(map(int,input().split(' ')))
has_card.sort()

M = int(input())
has_not_card = list(map(int,input().split()))


result= []


def binary_search(target):
    # 가지고 있는 카드 기준으로 함
    start = 0
    end = len(has_card)-1
    mid = (start+end)//2

    while (end-start >= 0):
        # 중간값과 같으면 1을 리턴함
        if has_card[mid] == target:
            return 1
        # 중간값보다 크면 오른쪽에 있으므로 중간기준으로 +1
        elif has_card[mid] < target:
            start = mid+1
        # 중간값보다 작으면 왼쪽에 있으므로 중간기준으로 -1
        elif has_card[mid] > target:
            end = mid-1
        # 한번 순회할 때 마다 시작, 끝값이 달라지므로 중간값을 다시 구함
        mid = (start+end) // 2
    # 검색해봐도 없으면 0 리턴
    return 0

for i in has_not_card:
    result.append(binary_search(i))
print(*result)