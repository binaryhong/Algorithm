def solution(n, m, section):
    answer = 0
    start = section[0]
    for i in range(1, len(section)):
        if section[i] - start + 1 > m:
            answer += 1
            start = section[i]
    answer += 1
    return answer