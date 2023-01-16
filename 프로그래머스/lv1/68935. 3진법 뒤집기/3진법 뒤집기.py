def solution(n):
    answer = ""
    while n >= 1:
        n, rest = divmod(n, 3)  # 몫, 나머지
        answer += str(rest)
    answer = int(answer, 3)
    return answer
