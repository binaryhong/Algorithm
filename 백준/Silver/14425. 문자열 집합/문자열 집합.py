n, m = map(int, input().split())
set_S = set(input() for _ in range(n))
count = 0

for _ in range(m):
    string_to_check = input()
    if string_to_check in set_S:
        count += 1

print(count)