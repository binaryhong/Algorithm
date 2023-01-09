def solution(dots):
    listA = []
    for i in range(0, len(dots)):
        for j in range(0, len(dots)):
            if i < j:
                # 기울기 = Y의 증가량 / X의 증가량
                try:
                    a = (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0])
                    a = round(a, 5)
                    listA.append(a)
                except ZeroDivisionError:
                    return 1
    cnt = 1
    for i in range(0, len(listA)):
        for j in range(0, len(listA)):
            if i != j:
                if listA[i] == listA[j]:
                    cnt = 1
                    return 1
                else:
                    cnt -= 100
    if cnt < 0:
        return 0