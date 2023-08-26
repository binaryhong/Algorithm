def solution(moneyList, m):
    start, end = 0, max(moneyList)

    while start <= end:
        mid = (start + end) // 2
        total = sum([min(mid, x) for x in moneyList])

        if total <= m:
            start = mid + 1
        else:
            end = mid - 1

    return end


N = int(input())
money = list(map(int, input().split()))
M = int(input())
print(solution(money, M))