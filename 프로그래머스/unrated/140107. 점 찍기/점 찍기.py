import math

def solution(k, d):
    cnt = 0
    for i in range(0, d + 1, k):
        j = math.sqrt(d*d - i*i)
        cnt += int(j // k) + 1
    return cnt
