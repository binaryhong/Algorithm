import math

n = int(input())
if n == 1:
    print(1)
else:
    low = 1
    high = int(math.sqrt(n // 3)) + 2  # 안전한 범위 확보
    
    while low < high:
        mid = (low + high) // 2
        if 3 * mid * (mid + 1) + 1 >= n:
            high = mid
        else:
            low = mid + 1
    print(high + 1)