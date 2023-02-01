def solution(n, arr1, arr2):
    binaryArr1 = []
    binaryArr2 = []
    answer = [""] * n
    for i in range(0, len(arr1)):
        if len(format(arr1[i], 'b')) < n:
            cnt0 = n - len(format(arr1[i], 'b'))
            binaryArr1.append("0" * cnt0 + format(arr1[i], 'b'))
        else:
            binaryArr1.append(format(arr1[i], 'b'))
    for i in range(0, len(arr2)):
        if len(format(arr2[i], 'b')) < n:
            cnt0 = n - len(format(arr2[i], 'b'))
            binaryArr2.append("0" * cnt0 + format(arr2[i], 'b'))
        else:
            binaryArr2.append(format(arr2[i], 'b'))
    for i in range(n):
        for j in range(n):
            for m in range(n):
                if i == j:
                    if binaryArr1[j][m] == "1" or binaryArr2[j][m] == "1":
                        answer[i] += "#"
                    if binaryArr1[j][m] == "0" and binaryArr2[j][m] == "0":
                        answer[i] += " "
    return answer