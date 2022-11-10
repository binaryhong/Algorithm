total = int(input())
n = int(input())
receipt = []
for i in range(n):
    a, b = map(int,input().split())
    receipt.append(a*b)
if sum(receipt) == total:
    print("Yes")
else:
    print("No")