def solution(x, n):
    cnt = 0
    answer = [x]
    while cnt < n-1:
        answer.append(answer[-1] + x)
        cnt += 1
    return answer