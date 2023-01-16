def solution(n):
    answer = [i*i for i in range(1, 10000000)]
    for i in range(len(answer)):
        if n == answer[i]:
            return answer[i+1]
    return -1