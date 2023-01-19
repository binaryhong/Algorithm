def solution(a, b):
    value = 0
    for i in range(0,len(a)):
        value += a[i]*b[i]
    return value