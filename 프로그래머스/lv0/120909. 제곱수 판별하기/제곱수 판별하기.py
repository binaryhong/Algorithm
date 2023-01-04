def solution(n):
    answer = []
    for i in range(1,10001):
        answer.append(i*i)
    if n in answer:
        return 1
    else:
        return 2