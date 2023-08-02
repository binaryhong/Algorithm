from heapq import heappush, heappop


def solution(n, k, enemy):
    h = []
    for i in range(len(enemy)):
        heappush(h, enemy[i])
        # print("h:", h)
        if len(h) > k:
            n -= heappop(h)
        if n < 0:
            return i
    return len(enemy)