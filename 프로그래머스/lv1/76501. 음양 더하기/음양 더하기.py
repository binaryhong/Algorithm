def solution(absolutes, signs):
    answer = []
    for i in range(len(absolutes)):
        if signs[i]:
            answer.append(absolutes[i])
        elif not signs[i]:
            answer.append(absolutes[i] * -1)
    return sum(answer)