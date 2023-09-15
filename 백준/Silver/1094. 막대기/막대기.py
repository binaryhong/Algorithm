x = int(input())
a = 64  # 원래 가지고 있는 막대
sumValue = 0
n = 64
cnt = 0
while x > 0:
    if n > x:
        n //= 2
    else:
        cnt += 1
        x -= n
print(cnt)
