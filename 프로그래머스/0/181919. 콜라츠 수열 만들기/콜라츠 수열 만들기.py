def solution(n):
    answer = [n]
    # 짝수
    while n != 1:
        if n % 2 == 0:
            n //= 2
        elif n % 2 == 1:
            n = 3 * n + 1
        answer.append(n)
    return answer