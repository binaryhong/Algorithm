def solution(survey, choices):
    """
    1 : RT TR
    2 : CF FC
    3 : JM MJ
    4 : AN NA

    3점: 매우 동의 매우 비동의
    2점: 동의 비동의
    1점: 약간 동의 약간 비동의
    0점: 모르겠음

    choices[i]: 1: 매우 비동의
    choices[i]: 2: 비동의
    choices[i]: 3: 약간 비동의
    choices[i]: 4: 모르겠음
    choices[i]: 5: 약간 동의
    choices[i]: 6: 동의
    choices[i]: 7: 매우 동의
    ...

    [5,3,2,7,5]
    =>
    ["약간 동의", "약간 비동의", "비동의", "매우 동의", "약간 동의"]
    ["AN", "CF", "MJ", "RT", "NA"]
    "AN"
    => 5이므로 약간 동의.
    => 비동의일경우 어피치 1점
    => 동의일경우 네오 1점
    => 네오 1점

    "CF"
    => 3이므로 약간 비동의
    =>비동의일경우 콘 1점
    =>동의일경우 프로도 1점
    => 콘 1점

    "MJ"
    => 2이므로 비동의
    => 비동의일경우 무지 2점
    => 동의일경우 제이지 2점
    => 무지 2점

    "RT"
    => 7이므로 매우 동의
    => 비동의일경우 라이언 3점
    => 동의일경우 튜브 3점
    => 튜브 3점

    "NA"
    => 5이므로 약간 동의
    => 비동의일경우 네오 1점
    => 동의일경우 어피치 1점
    => 어피치 1점

    문자열 [i][0]항은 비동의
    문자열 [i][1]항은 동의
    """
    answer = ""
    scoreList = [["R", 0], ["T", 0], ["C", 0], ["F", 0],
                 ["J", 0], ["M", 0], ["A", 0], ["N", 0]]
    for i in range(len(choices)):
        for j in range(8):
            if choices[i] == 1:  # 매우 비동의
                if survey[i][0] == scoreList[j][0]:
                    scoreList[j][1] += 3
            elif choices[i] == 2:  # 비동의 # MJ
                if survey[i][0] == scoreList[j][0]:
                    scoreList[j][1] += 2
            elif choices[i] == 3:  # 약간 비동의
                if survey[i][0] == scoreList[j][0]:
                    scoreList[j][1] += 1
            elif choices[i] == 4:  # 모르겠음
                if survey[i][0] == scoreList[j][0]:
                    scoreList[j][1] += 0
            elif choices[i] == 5:  # 약간 동의
                # 약간 동의 "AN"
                # => 5이므로 약간 동의.
                # => 비동의일경우 어피치 1점
                # => 동의일경우 네오 1점
                # => 네오 1점
                if survey[i][1] == scoreList[j][0]:
                    scoreList[j][1] += 1
            elif choices[i] == 6:  # 동의
                if survey[i][1] == scoreList[j][0]:
                    scoreList[j][1] += 2
            elif choices[i] == 7:  # 매우 동의
                if survey[i][1] == scoreList[j][0]:
                    scoreList[j][1] += 3
    for i in range(0, 8, 2):
        if scoreList[i][1] > scoreList[i + 1][1]:
            answer += scoreList[i][0]
        elif scoreList[i][1] < scoreList[i + 1][1]:
            answer += scoreList[i + 1][0]
        elif scoreList[i][1] == scoreList[i + 1][1]:
            if ord(scoreList[i][0]) > ord(scoreList[i + 1][0]):
                answer += scoreList[1][0]
            elif ord(scoreList[i][0]) < ord(scoreList[i + 1][0]):
                answer += scoreList[i][0]
    return answer
