def solution(priorities, location):
    from collections import deque
    answer = 0
    printerList_with_index = [[value, idx] for idx, value in enumerate(priorities)]
    dq = deque(printerList_with_index)
    while True:
        max_value = max(row[0] for row in dq)
        if dq[0][0] == max_value:
            printed = dq.popleft()
            answer += 1
            if printed[1] == location:
                return answer
        else:
            dq.append(dq.popleft())