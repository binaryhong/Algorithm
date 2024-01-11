N = int(input())
c = []
result = []
for i in range(N):
    b = int(input())
    c.append(b)
c.sort(reverse=True)
for i in range(len(c)):
    result.append(c[i]*(i+1))
print(max(result))