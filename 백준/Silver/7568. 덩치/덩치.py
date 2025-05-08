n = int(input())
people = []
for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

ranks = []
for i in range(n):
    count = 0
    for j in range(n):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            count += 1
    ranks.append(str(count + 1))

print(' '.join(ranks))