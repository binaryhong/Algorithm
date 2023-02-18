def solution(n, a, b):
    answer = 1
    while 1:
        if (a % 2 == 0 and a - 1 == b) or (a % 2 == 1 and a + 1 == b):
            return answer

        a = ton(a)
        b = ton(b)

        answer += 1


def ton(x):
    if x % 2 == 0:
        return int(x / 2)
    else:
        return int((x / 2) + 1)