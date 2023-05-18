import math


def solution(str1, str2):
    listStr1 = []
    listStr2 = []
    answerStr1 = []
    answerStr2 = []
    # 두 글자씩 리스트에 넣는 과정
    for i in range(len(str1) - 1):
        value = ""
        for j in range(i, i + 2):
            value += str1[j]
            if len(value) == 2:
                listStr1.append(value)
    for i in range(len(str2) - 1):
        value = ""
        for j in range(i, i + 2):
            value += str2[j]
            if len(value) == 2:
                listStr2.append(value)

    # 두글자씩 넣은 리스트에서 알파벳으로 이루어진것만 추출 및 소문자 변환.
    for i in range(len(listStr1)):
        cnt = 0
        value = ""
        for j in range(len(listStr1[i])):
            if listStr1[i][j].isalpha():
                value += listStr1[i][j].lower()
                cnt += 1
            if cnt == 2:
                answerStr1.append(value)

    for i in range(len(listStr2)):
        cnt = 0
        value = ""
        for j in range(len(listStr2[i])):
            if listStr2[i][j].isalpha():
                value += listStr2[i][j].lower()
                cnt += 1
            if cnt == 2:
                answerStr2.append(value)

    # 교집합과 합집합 계산
    inter = set(answerStr1) & set(answerStr2)
    union = set(answerStr1) | set(answerStr2)

    inter_cnt = sum([min(answerStr1.count(i), answerStr2.count(i)) for i in inter])
    union_cnt = sum([max(answerStr1.count(i), answerStr2.count(i)) for i in union])
    # 자카드 유사도 계산
    if union_cnt == 0:
        return 65536
    else:
        return math.floor(inter_cnt / union_cnt * 65536)