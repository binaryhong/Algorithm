def solution(s):
    answer = []
    if len(s) < 2:
        return 0

    for i in s:
        if not answer:
            answer.append(i)
        elif answer[-1] == i:
            answer.pop()
        elif answer[-1] != i:
            answer.append(i)
    if len(answer) > 0:
        return 0
    else:
        return 1