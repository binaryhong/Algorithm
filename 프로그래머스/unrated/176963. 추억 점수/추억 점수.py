def solution(name, yearning, photo):
    answer = []
    for people in photo:
        sumValue = 0
        for person in people:
            if person in name:
                sumValue +=yearning[name.index(person)]
        answer.append(sumValue)
    return answer