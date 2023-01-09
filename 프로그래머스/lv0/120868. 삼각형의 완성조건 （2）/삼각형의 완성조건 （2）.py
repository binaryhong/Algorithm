def solution(sides):
    answer = []
    for i in range(1,sum(sides)):
        # sides가 작은 길이
        if max(sides) < i:
            if sum(sides) > i:
                answer.append(i)
        # max(sides)가 가장 큰 길이
        elif i < max(sides):
            if i+min(sides) > max(sides):
                answer.append(i)
        elif i == max(sides):
            if i + min(sides) > max(sides):
                answer.append(i)
    return len(answer)
