def solution(k, score):
    honor = []
    answer = []
    for i, value in enumerate(score):
        if len(honor) < k:
            honor.append(value)
            answer.append(min(honor))
        elif len(honor) >= k:
            honor.append(value)
            honor.sort(reverse=True)
            honor.pop()
            answer.append(min(honor))
    return answer