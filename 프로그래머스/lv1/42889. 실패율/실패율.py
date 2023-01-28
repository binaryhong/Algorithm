def solution(N, stages):
    result = {}
    lenStages = len(stages)
    for i in range(1, N + 1):
        if lenStages != 0:
            count = stages.count(i)
            result[i] = count / lenStages
            lenStages -= count
        else:
            result[i] = 0
    # print(result)
    return sorted(result, key=lambda x: result[x], reverse=True)
    #  딕셔너리 value값에 따른 내림차순 정렬 후 key값만 출력