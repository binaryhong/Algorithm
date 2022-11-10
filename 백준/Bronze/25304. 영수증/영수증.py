total = int(input())
n = int(input())
receipt = []
for i in range(n):
    a, b = map(int,input().split())
    sumValue = a * b
    receipt.append(sumValue)
if sum(receipt) == total:
    print("Yes")
else:
    print("No")