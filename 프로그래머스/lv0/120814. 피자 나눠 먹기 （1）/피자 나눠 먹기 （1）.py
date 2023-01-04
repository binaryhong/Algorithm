def solution(n):
    for i in range(0, 101):
        if n % 7 == 0:
            return int(n/7)
        else:
            return int(n / 7 + 1)