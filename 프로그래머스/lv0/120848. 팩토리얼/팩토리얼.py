def solution(n):
    a = [0]
    j = 1
    for i in range(1,11):
        j = j * i
        a.append(j)
    if n in a:
        return a.index(n)
    else:
        for i in range(len(a)):
            if n < a[i]:
                return i-1