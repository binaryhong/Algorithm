import sys

a, b = map(int, sys.stdin.readline().split())
c = int(input())
d = c // 60  # 몫. 추가 필요시간 계산위해.
e = c % 60  # 나머지.
if 60 < b + e < 120:
    a += d + 1
    if a == 24:
        a = 0
        print(a, b + e - 60)
    elif a > 24:
        print(a-24, b + e - 60)
    else:
        print(a, b + e - 60)
elif b + e == 60:
    a += d + 1
    b = 0
    if a == 24:
        a = 0
        print(a, b)
    elif a > 24:
        print(a-24, b)
    else:
        print(a, b)
else:
    a += d
    if a == 24:
        a = 0
        print(a, b+e)
    elif a > 24:
        print(a-24, b + e)
    else:
        print(a, b+e)
