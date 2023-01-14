def solution(numlist, n):
    listA = []
    answer = []
    for i in range(len(numlist)):
        if n-numlist[i] < 0:
            listA.append([(n-numlist[i]) * -1,numlist[i]])
        elif n-numlist[i] > 0:
            listA.append([n-numlist[i], numlist[i]])
        else:
            listA.append([n-numlist[i], numlist[i]])
    listA.sort(key=lambda x:x[0])
    for i in range(len(listA)):
        for j in range(len(listA)):
            if i < j:
                if listA[i][0] == listA[j][0]:
                    listA.sort(key=lambda x: (x[0], -x[1]))
    for i in range(len(listA)):
        answer.append(listA[i][1])
    return answer