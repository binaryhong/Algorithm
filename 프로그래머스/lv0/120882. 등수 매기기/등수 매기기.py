def solution(score):
    answer = []
    final = [len(score)] * len(score)
    for i in range(len(score)):
        answer.append(sum(score[i]))

    for i in range(len(answer)):
        for j in range(len(answer)):
            if i != j:
                if answer[i] >= answer[j]:
                    final[i] = final[i] - 1
    return final