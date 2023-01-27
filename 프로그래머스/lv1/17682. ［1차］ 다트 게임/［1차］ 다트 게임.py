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
        # 10을 한 리스트에 넣기위한 코드. 1과 0 
        if dartResult[i] == "D":
            sumValue = dartList[-1]
            dartList[-1] = int(sumValue) * int(sumValue)
        # D면 제곱.
        if dartResult[i] == "T":
            sumValue = dartList[-1]
            dartList[-1] = int(sumValue) * int(sumValue) * int(sumValue)
        # T면 세제곱.
        if dartResult[i] == "*":
            starCnt += 1
            for j in range(0, len(dartList)):
                dartList[j] *= 2
        if dartResult[i] == "#":
            dartList[-1] *= -1
    # 문제조건 *이 마지막에 있으면 첫항은 *2 하지않음.
    if starCnt == 1:
        if dartResult[-1] == "*":
            dartList[0] //= 2
    if starCnt == 2:
        if dartResult[-1] == "*":
            dartList[0] //= 2
    if starCnt == 3:
        if dartResult[-1] == "*":
            dartList[0] //= 2
    return sum(dartList)
