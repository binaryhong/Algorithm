from collections import deque
count = int(input())
printerList = []
answer = 0
for i in range(0,count):
    answer = 0
    N, M = map(int,input().split())
    printerList = list(map(int,input().split()))
    printerList_with_index = [[value, idx] for idx, value in enumerate(printerList)]
    dq = deque(printerList_with_index)
    while True:
        max_value = max(row[0] for row in dq)
        if dq[0][0] == max_value:
            printed = dq.popleft()
            answer += 1
            if printed[1] == M:
                print(answer)
                break
        else:
            dq.append(dq.popleft())