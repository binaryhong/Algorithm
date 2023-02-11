def solution(s):
    stack = []
    if len(s) < 2:
        return 0

    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        elif stack[-1] != i:
            stack.append(i)
    if len(stack) > 0:
        return 0
    else:
        return 1