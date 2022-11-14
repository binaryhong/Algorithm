import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
_dict = {}  # 속도는 dictionary!
for i in range(len(a)):
    _dict[a[i]] = 0  # 아무 숫자로 mapping

for j in range(m):
    if b[j] not in _dict:
        print("0", end=' ')
    else:
        print("1", end=' ')