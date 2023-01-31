def solution(participant, completion):
    answer = {}
    # {'leo': 1, 'kiki': 1, 'eden': 1}와 같은 형태로 딕셔너리 생성
    # 문자열 개수 생성 딕셔너리 (동명이인 포함)
    for name in participant:
        if name in answer:
            answer[name] += 1
        else:
            answer[name] = 1

    # completion 리스트에 있으면 answer 딕셔너리 개수 감소.
    for name in completion:
        if name in answer:
            answer[name] -= 1

    # 문제조건 단 한명의 선수를 제외하고는 모든 선수가 마라톤 완주.
    for name in answer:
        if answer[name] > 0:
            return name