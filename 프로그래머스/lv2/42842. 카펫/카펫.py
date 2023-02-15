def solution(brown, yellow):
    answer = []
    sumValue = brown + yellow
    for i in range(1,sumValue+1):
        if sumValue % i == 0:
            if (i-2) * (sumValue //i -2) == yellow:
                if i >= sumValue //i :
                    answer.append([i, sumValue // i])
    returnList = []
    for i in range(1):
        for j in range(2):
            returnList.append(answer[i][j])
    return returnList