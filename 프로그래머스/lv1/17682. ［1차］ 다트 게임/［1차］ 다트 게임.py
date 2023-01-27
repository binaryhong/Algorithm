def solution(dartResult):
    dartResult.split()
    dartList = []
    starCnt = 0
    digitValue = ""
    for i in range(0, len(dartResult)):
        if dartResult[i].isdigit():
            digitValue += dartResult[i]
        elif dartResult[i].isalpha() or dartResult[i] == "*" or dartResult[i] == "#":
            if digitValue != "":
                dartList.append(int(digitValue))
            digitValue = ""
        if dartResult[i] == "D":
            sumValue = dartList[-1]
            # print("시작 dartList:", dartList)
            # print("sumValue:", sumValue)
            # print("D : dartList:", dartList)
            dartList[-1] = int(sumValue) * int(sumValue)
            # print("D dartList:", dartList)
        if dartResult[i] == "T":
            sumValue = dartList[-1]
            dartList[-1] = int(sumValue) * int(sumValue) * int(sumValue)
            # print("dartList:", dartList)
        if dartResult[i] == "*":
            starCnt += 1
            for j in range(0, len(dartList)):
                dartList[j] *= 2
        if dartResult[i] == "#":
            dartList[-1] *= -1
            # print("dartList:", dartList)
    if starCnt == 1:
        if dartResult[-1] == "*":
            dartList[0] //= 2
    if starCnt == 2:
        if dartResult[-1] == "*":
            dartList[0] //= 2
    if starCnt == 3:
        if dartResult[-1] == "*":
            dartList[0] //= 2
    # print("final:", dartList)
    return sum(dartList)