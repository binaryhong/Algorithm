N, t, p = map(int, input().split())
if N > 0:
    score = list(map(int, input().split()))
    if N == p and score[-1] >= t:
        print(-1)
    else:
        res = N + 1
        for i in range(N):
            if score[i] <= t:
                res = i + 1
                break
        print(res)
if N <= 0:
    print(1)