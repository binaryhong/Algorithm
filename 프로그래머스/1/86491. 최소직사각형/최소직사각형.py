def solution(sizes):
    sizes = [[max(a, b), min(a, b)] for a, b in sizes]
    sizes.sort(key=lambda x: x[0], reverse=True)
    max_value1 = max(row[0] for row in sizes)
    max_value2 = max(row[1] for row in sizes)
    return max_value1 * max_value2