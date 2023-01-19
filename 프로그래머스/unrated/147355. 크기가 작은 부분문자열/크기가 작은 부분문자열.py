def solution(t, p):
    listA = []
    for i in range(0, len(t)):
        listA.append(t[i:i+len(p)])
    cnt = 0
    for i in range(0,len(listA)):
        if len(listA[i]) == len(p):
            if listA[i] <= p:
                cnt += 1
    return cnt
