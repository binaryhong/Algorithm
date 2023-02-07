def solution(n):
    answer = 0
    for i in range(1,n+1):
        sumValue = 0
        for j in range(i, n+1):
            sumValue += j
            if sumValue == n:
                answer += 1
                break
            elif sumValue > n:
                break

    return answer