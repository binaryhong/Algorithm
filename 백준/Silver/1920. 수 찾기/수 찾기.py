from sys import stdin

n = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
k = stdin.readline()
M = map(int, stdin.readline().split())


def binary(a, b, c, d):
    if c > d:  # start > end
        return 0
    m = (c + d) // 2  # middle = (start+end) // 2
    if a == b[m]:
        return 1
    elif a < b[m]:
        return binary(a, b, c, m - 1)
    else:
        return binary(a, b, m + 1, d)


for l in M:
    start = 0
    end = len(N) - 1
    print(binary(l, N, start, end))