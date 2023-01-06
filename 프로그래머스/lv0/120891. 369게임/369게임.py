def solution(order):
    cnt = 0
    strOrder = str(order)
    for i in range(len(strOrder)):
        if strOrder[i] == "3":
            cnt += 1
        elif strOrder[i] == "6":
            cnt += 1
        elif strOrder[i] == "9":
            cnt += 1
    return cnt