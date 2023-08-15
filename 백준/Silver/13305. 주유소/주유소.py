N = int(input())
distance = list(map(int, input().split()))
litter = list(map(int, input().split()))
result = 0
for i in range(N-1):
    if litter[i] < litter[i+1]:
        litter[i+1] = litter[i]
    result += litter[i] * distance[i]
print(result)