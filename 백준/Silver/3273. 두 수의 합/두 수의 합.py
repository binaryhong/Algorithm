n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

numbers.sort()

count = 0
left, right = 0, n - 1

while left < right:
    current_sum = numbers[left] + numbers[right]

    if current_sum == x:
        count += 1
        left += 1
        right -= 1
    elif current_sum < x:
        left += 1
    else:
        right -= 1

print(count)