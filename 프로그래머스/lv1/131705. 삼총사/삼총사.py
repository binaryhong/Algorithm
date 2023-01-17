from itertools import combinations
def solution(number):
    new_list = list(combinations(number, 3))
    cnt = 0
    for i in range(len(new_list)):
        if sum(new_list[i]) == 0:
            cnt += 1
    return cnt