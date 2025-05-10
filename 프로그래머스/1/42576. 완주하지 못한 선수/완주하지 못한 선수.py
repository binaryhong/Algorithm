def solution(participant, completion):
    participant_dict = {}

    # 참가자 명단 카운트
    for name in participant:
        if name in participant_dict:
            participant_dict[name] += 1
        else:
            participant_dict[name] = 1

    # 완주자 명단 카운트 빼기
    for name in completion:
        participant_dict[name] -= 1

    # 값이 1인(완주 못한) 사람 찾기
    for name, count in participant_dict.items():
        # print("name:", name, "count:", count)
        if count > 0:
            return name