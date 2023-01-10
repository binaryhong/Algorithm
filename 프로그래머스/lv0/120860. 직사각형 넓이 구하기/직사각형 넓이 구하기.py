def solution(dots):
    garo = 1
    sero = 1
    for i in range(0, len(dots)):
        for j in range(len(dots)):
            if i < j:
                if dots[i][0] == dots[j][0]:
                    garo = abs(dots[i][1] - dots[j][1])
                elif dots[i][1] == dots[j][1]:
                    sero = abs(dots[i][0] - dots[j][0])

    return garo * sero