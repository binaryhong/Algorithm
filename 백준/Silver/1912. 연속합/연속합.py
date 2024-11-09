n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
sum_value = 0
for i in range(n):
    sum_value += a[i]
    dp[i] = sum_value
    if sum_value < 0:
        sum_value = 0
if all(value < 0 for value in a):
    print(max(a))
else:
    print(max(dp))