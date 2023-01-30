n = int(input())
s = list(input() for _ in range(n))
for i in range(0, len(s)):
    s[i] = s[i][::-1]
bList = [""] * n
k = 1
for i in range(1,len(s[0])+1):
    for j in range(0,n):
        bList[j] = s[j][0:i]
    if len(list(set(bList))) == n:
        print(len(bList[0]))
        break