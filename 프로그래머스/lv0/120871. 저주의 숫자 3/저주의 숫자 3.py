def solution(n):
    aList = [i for i in range(1, 10001)]
    temp = aList[::]

    for value in temp:
        if value % 3 == 0:
            aList.remove(value)
        if value // 10 == 3:
            try:
                aList.remove(value)
            except ValueError:
                pass
        if 30 <= value // 10 < 40:
            try:
                aList.remove(value)
            except ValueError:
                pass
        if 300 <= value // 10 < 400:
            try:
                aList.remove(value)
            except ValueError:
                pass
        if 3000 <= value // 10 < 4000:
            try:
                aList.remove(value)
            except ValueError:
                pass
        a = "".join(str(value))
        for j in range(len(a)):
            try:
                if "3" in a:
                    aList.remove(int(a))
            except ValueError:
                pass
    return aList[n-1]