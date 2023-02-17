n = int(input())
list1 = list(map(int, input().split()))
list1.sort()
sum_value = 0
for i in range(len(list1)):
    sum_value += sum(list1[:i+1])
print(sum_value)