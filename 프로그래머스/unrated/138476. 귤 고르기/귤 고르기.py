from collections import Counter


def solution(k, tangerine):
    count = Counter(tangerine)
    answer = 0
    sort_ = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for i in sort_:
        k -= i[1]
        answer += 1

        if k <= 0:
            break
    return answer