def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        sumValue = []
        for i, j in zip(a, b):
            sumValue.append(i + j)

        answer.append(sumValue)
    return answer