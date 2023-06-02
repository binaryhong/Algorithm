def solution(n, k):
    answer = []
    numbers = [i for i in range(1, n+1)]
    factorial = [1] * n
    for i in range(1, n):
        factorial[i] = factorial[i-1] * i
    k -= 1
    for i in range(n, 0, -1):
        index = k // factorial[i-1]
        k %= factorial[i-1]
        answer.append(numbers.pop(index))
    return answer