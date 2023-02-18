def solution(n):
    aList = [0, 1, 1, 2]
    while len(aList) < n+1000:
        aList.append(sum(aList[-2:]))
    return aList[n] % 1234567