def solution(a, b):
    answer = 0
    a.sort(reverse=True)
    b.sort()
    for i in range(len(a)):
        answer += (a[i] * b[i])
    return answer