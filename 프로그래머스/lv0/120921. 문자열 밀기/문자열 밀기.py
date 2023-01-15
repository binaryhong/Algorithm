from collections import deque
def solution(A, B):
    deq = deque(list(A))
    cnt = 0
    if A == B:
        return 0
    elif A != B:
        for i in range(len(A)):
            deq.appendleft((deq.pop()))
            cnt +=1
            if "".join(deq) == B:
                return cnt
        return -1