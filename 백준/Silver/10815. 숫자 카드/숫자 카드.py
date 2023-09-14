N = int(input())
a = set(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
for i in b:
    if i in a:
        print(1, end=" ")
    else:
        print(0, end=" ")