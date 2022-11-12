person = list(map(int,input().split()))
arr = list(map(int, input().split()))
arr.sort()
for i in range(person[1]-1):
    arr.pop()
print(arr[-1])