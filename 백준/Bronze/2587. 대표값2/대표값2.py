arr = []
for i in range(5):
    arr.append(int(input()))
arr.sort()
print(sum(arr)//5) # 평균
print(arr[2]) # 중앙값