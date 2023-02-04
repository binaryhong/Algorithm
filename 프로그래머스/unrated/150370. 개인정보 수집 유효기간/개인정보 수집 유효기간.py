def solution(today, terms, privacies):
    todayList = list(map(int, today.split(".")))
    # print("todayList:", todayList)
    termsList = [value.replace(' ', '') for value in terms]
    termsNumberList = []
    termsAlphaList = []
    value = ""
    answer = []

    # terms를 알파벳과 숫자를 분리해서 termsAlphaList, termsNumberList에 저장
    for i in range(len(termsList)):
        for j in range(len(termsList[i])):
            if termsList[i][j].isalpha():
                if value:
                    termsNumberList.append(int(value))
                    value = ""
                termsAlphaList.append(termsList[i][j])
            if termsList[i][j].isdigit():
                value += termsList[i][j]  # 10을 인식하기 위해 str로 더함.

    termsNumberList.append(int(value))  # 마지막항을 더해야함.

    value = ""
    privaciesNum = []
    privaciesYear = []
    privaciesMonth = []
    privaciesDay = []
    privaciesAlpha = []
    privacyList = []

    # privacies를 알파벳과 숫자를 분리해서 privaciesAlpha, privaciesNum에 저장
    for i in range(len(privacies)):
        for j in range(len(privacies[i])):
            if privacies[i][j].isalpha():
                if value:
                    privaciesNum.append(value)
                    value = ""
                privaciesAlpha.append(privacies[i][j])
            if privacies[i][j].isdigit():
                value += privacies[i][j]
    # privaciesNum.append(value)

    # privaciesNum을 년, 월, 일로 분리해서 저장.
    for i in range(len(privaciesNum)):
        privaciesMonth.append(privaciesNum[i][4:])
        privaciesYear.append(int(privaciesNum[i][:4]))
        if privaciesMonth[i][0] == '0':
            privaciesDay.append(int(privaciesMonth[i][2:]))
            privaciesMonth[i] = int(privaciesMonth[i][1:2])
        else:
            privaciesDay.append(int(privaciesMonth[i][2:]))
            privaciesMonth[i] = int(privaciesMonth[i][:2])
        privacyList.append(privaciesYear[i])
        privacyList.append(privaciesMonth[i])
        privacyList.append(privaciesDay[i])

    # print("privacyList:", privacyList)
    # privaciesAlpha에 terms 숫자를 저장
    for i in range(len(privaciesAlpha)):
        for j in range(len(termsAlphaList)):
            if privaciesAlpha[i] == termsAlphaList[j]:
                privaciesAlpha[i] = termsNumberList[j]
    # print("privaciesAlpha:", privaciesAlpha)
    for i, value in enumerate(privaciesAlpha): # terms의 유효기간이 2년이 넘어갈경우.
        privacyList[i * 3 + 1] += value % 12
        if privacyList[i * 3 + 1] > 12:
            privacyList[i * 3 + 1] -= 12
            privacyList[i * 3] += 1
        privacyList[i * 3] += value // 12

    for j in range(len(privaciesAlpha)):
        if todayList[0] > privacyList[j * 3]:  # 유효기간 년도가 지남
            answer.append(j + 1)
        elif todayList[0] == privacyList[j * 3]:  # 연도가 같다면
            if todayList[1] > privacyList[j * 3 + 1]:  # 현재의 월이 더 지남.
                answer.append(j + 1)
            elif todayList[1] == privacyList[j * 3 + 1]:  # 월이 같다면
                if todayList[2] >= privacyList[j * 3 + 2]:  # 오늘이 유효기간의 날과 같거나 더 빠르다면
                    answer.append(j + 1)
        elif todayList[0] < privacyList[j * 3]:  # 유효기간 지나지 않음
            pass
    # print("privacyList:", privacyList)
    # print("termsAlphaList:", termsAlphaList)
    # print("termsNumberList:", termsNumberList)
    return answer
