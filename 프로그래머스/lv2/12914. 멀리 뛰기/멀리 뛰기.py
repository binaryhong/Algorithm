def solution(n):
    answer = [0] * (n + 1)
    answer[0] = 1
    answer[1] = 2
    for i in range(2, n):
        answer[i] = answer[i - 1] + answer[i - 2]
    return answer[n-1] % 1234567