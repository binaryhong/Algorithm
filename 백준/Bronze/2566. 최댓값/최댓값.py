arr= []
maxList = []

for i in range(9):
    arr.append(list(map(int,input().split())))
    maxList.append(max(arr[i]))
print(max(maxList))
for i in range(9):
    for j in range(9):
        if max(maxList) == arr[i][j]:
            print(i+1,j+1)