def solution(num_list):
    for value in num_list:
        if value < 0:
            return num_list.index(value)
    return -1