def solution(s):
    from collections import deque
    q = deque(s)
    answer = 0
    if len(q) % 2 == 1:
        return 0
    for i in range(len(list(q))):
        stack = []
        for j in range(0,len(q)):
            if stack:
                if stack[-1] == "[" and q[j] == "]":
                    stack.pop()
                elif stack[-1] == "{" and q[j] == "}":
                    stack.pop()
                elif stack[-1] == "(" and q[j] == ")":
                    stack.pop()
                else:
                    stack.append(q[j])
            else:
                stack.append(q[j])
        if len(stack) == 0:
            answer += 1
        q.appendleft(q.pop())

    return answer