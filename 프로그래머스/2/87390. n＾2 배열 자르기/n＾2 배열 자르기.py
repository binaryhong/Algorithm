def solution(n, left, right):
    answer = []
    for k in range(left, right+1):
        i = k // n + 1  # 행 인덱스(1-based)
        j = k % n + 1   # 열 인덱스(1-based)
        answer.append(max(i, j))
    return answer