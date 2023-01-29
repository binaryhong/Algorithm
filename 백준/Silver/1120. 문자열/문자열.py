a, b = map(str, input().split())
cnt = 0
differentList = []
if len(a) == len(b):
    for i in range(0, len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)

if len(a) != len(b):
    for i in range(0, len(b)-len(a)+1):
        for j in range(len(a)):
            if a[j] != b[i:i+len(a)][j]:
                cnt += 1
        differentList.append(cnt)
        cnt = 0
    print(min(differentList))