def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            element = 0
            for k in range(len(arr1[0])):
                element += arr1[i][k] * arr2[k][j]
            row.append(element)
        answer.append(row)
    return answer