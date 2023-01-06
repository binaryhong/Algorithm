def solution(array):
    answer = []
    maxValue = -1
    cnt = 0
    for i in range(len(array)):
        answer.append([array[i], array.count(array[i])])
    listA = list(set(map(tuple, answer)))
    for i in range(0, len(listA)):
        maxValue = max(listA[i][1], maxValue)
    for i in range(0,len(listA)):
        if listA[i][1] == maxValue:
            returnValue = listA[i][0]
    for i in range(0, len(listA)):
        if maxValue == listA[i][1]:
            cnt += 1
    if cnt > 1:
        return -1
    else:
        return returnValue