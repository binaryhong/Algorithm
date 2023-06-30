def solution(order):
    n = len(order)
    stack = []
    idx = 0
    for i in range(1, n + 1):
        stack.append(i)
        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
    return idx