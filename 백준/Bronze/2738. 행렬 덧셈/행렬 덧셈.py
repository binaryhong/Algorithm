a, b = [], []
N, M = map(int,input().split())

for _ in range(N):
    row = list(map(int,input().split()))
    a.append(row)

for _ in range(N):
    row = list(map(int,input().split()))
    b.append(row)

for row in range(N):
    for col in range(M):
        print(a[row][col]+b[row][col], end = " ")
    print()