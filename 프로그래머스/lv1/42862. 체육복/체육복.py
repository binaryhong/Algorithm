def solution(n, lost, reserve):
    answer = 0
    lost_dic = {}
    for i in range(1, n+1): lost_dic[i] = 1
    for i in reserve: lost_dic[i] += 1
    for i in lost: lost_dic[i] -= 1
    for i in range(1, n + 1):
        if i >= 2 and lost_dic[i] == 0 and lost_dic[i -1] == 2:
            lost_dic[i - 1] = 1
            lost_dic[i] = 1
        if i < n and lost_dic[i] == 0 and lost_dic[i + 1] == 2:
            lost_dic[i + 1] = 1
            lost_dic[i] = 1
    for i in range(1, len(lost_dic)+ 1):
        if lost_dic[i] >= 1:
            answer += 1
    return answer