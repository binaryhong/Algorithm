def solution(k, m, score):
    # k 사과의 최대 점수
    # m  한 상자에 들어가는 사과의 수
    # score 사과들의 점수
    appleBox = []
    new_score = []
    sumValue = 0
    score.sort(reverse=True)
    for i in range(0, len(score)):
        new_score.append(score[i])
        if len(new_score) == m:
            appleBox.append(new_score)
            new_score = []
    for i in range(0, len(appleBox)):
        sumValue += min(appleBox[i]) * m
    return sumValue