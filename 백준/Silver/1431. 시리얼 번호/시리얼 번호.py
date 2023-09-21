def sum_of_digits(s):
    return sum(int(x) for x in s if x.isdigit())


N = int(input())
guitar = []
for _ in range(N):
    guitar.append(input())
sorted_list = sorted(guitar, key=lambda x: (len(x), sum_of_digits(x), x, ''.join(filter(str.isdigit, x))))
print(*sorted_list)