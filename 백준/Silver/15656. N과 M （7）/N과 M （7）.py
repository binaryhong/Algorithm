from itertools import product
n, m = map(int,input().split())
exList = list(map(int,input().split()))
prod = list(product(exList, repeat=m))
sorted_prod = sorted(prod)
for item in sorted_prod:
    print(*item)