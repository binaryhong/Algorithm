def solution(answers):
    aList = [1, 2, 3, 4, 5] * len(answers)
    aCnt = 0
    bList = [2, 1, 2, 3, 2, 4, 2, 5] * len(answers)
    bCnt = 0
    cList = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(answers)
    cCnt = 0
    for i in range(len(answers)):
        if answers[i] == aList[i]:
            aCnt += 1
        if answers[i] == bList[i]:
            bCnt += 1
        if answers[i] == cList[i]:
            cCnt += 1
    if aCnt == bCnt == cCnt:
        return [1, 2, 3]
    elif aCnt == bCnt and aCnt > cCnt:
        return [1, 2]
    elif aCnt == cCnt and aCnt > bCnt and cCnt > bCnt:
        return [1, 3]
    elif bCnt == cCnt and bCnt > aCnt and cCnt > aCnt:
        return [2, 3]
    elif aCnt > bCnt >= cCnt or aCnt > cCnt >= bCnt:
        return [1]
    elif bCnt > cCnt >= aCnt or bCnt > aCnt >= cCnt:
        return [2]
    elif cCnt > bCnt >= aCnt or cCnt > aCnt >= bCnt:
        return [3]