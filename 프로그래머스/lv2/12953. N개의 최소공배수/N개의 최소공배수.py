def solution(arr):
    arr.sort()
    for i in range(1, 1000000):
        cnt = 0
        maxValue = max(arr) * i
        for j in range(len(arr)):
            if maxValue % arr[j] == 0:
                cnt += 1
        if cnt == len(arr):
            return maxValue