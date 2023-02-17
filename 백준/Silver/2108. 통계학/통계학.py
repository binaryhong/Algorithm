import sys
from collections import Counter
n = int(sys.stdin.readline())
aList = []
for _ in range(0, n):
    k = int(sys.stdin.readline().rstrip())
    aList.append(k)
aList.sort()
cnt = Counter(aList).most_common(2)
print(round(sum(aList) / len(aList)))  # 산술평균
print(aList[n // 2])  # 중앙값 n이 홀수이므로 2로 나누어도 충분함.
if len(aList) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(aList) - min(aList))