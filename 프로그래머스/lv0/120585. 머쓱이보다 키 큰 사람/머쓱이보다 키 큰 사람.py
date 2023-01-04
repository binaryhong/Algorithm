def solution(array, height):
    cnt = 0
    for i in range(len(array)):
        if height-array[i] < 0:
            cnt += 1
    return cnt