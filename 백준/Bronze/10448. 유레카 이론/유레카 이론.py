from itertools import combinations_with_replacement

N = int(input())
testCase = []
gause = []

for i in range(N):
    testCase.append(int(input()))
# print(testCase)
for i in range(1, 125):
    gause.append((i * (i + 1) // 2))
# print(gause)

permutationsList = []
for i in combinations_with_replacement(gause, 3):
    permutationsList.append(sum(i))

for i in range(len(testCase)):
    if testCase[i] in permutationsList:
        print(1)
    else:
        print(0)