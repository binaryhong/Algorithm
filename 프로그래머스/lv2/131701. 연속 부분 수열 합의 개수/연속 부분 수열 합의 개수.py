def solution(elements):
    n = len(elements)
    sums = set()
    for i in range(n):
        total = 0
        for j in range(n):
            total += elements[(i + j) % n]
            sums.add(total)
    return len(sums)