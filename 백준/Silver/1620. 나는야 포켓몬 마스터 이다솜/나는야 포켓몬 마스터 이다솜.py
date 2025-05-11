import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
c = []
d = []
e = {}
for i in range(a):
    c.append(sys.stdin.readline().rstrip())  # 리스트에 포켓몬이름 저장.
e = {string: i+1 for i, string in enumerate(c)}
for i in range(b):
    d.append(sys.stdin.readline().rstrip())

for value in d:
    if value.isdigit():
        print(c[int(value)-1])
    elif str(value).isalpha():
        print(e.get(value))