from itertools import permutations
def solution(spell, dic):
    answer = []
    result = ""
    resultList = []
    for i in permutations(spell, len(spell)):
        answer.append(list(i))
    # print("answer:",answer)
    for i in range(0, len(answer)):
        for j in range(0, len(answer[i])):
            result += answer[i][j]
        # print("result:", result)
        if result in dic:
            resultList.append(result)
        result = ""
    # print(resultList)
    if resultList:
        return 1
    return 2