N = int(input())
student_list = []

for _ in range(N):
    line = input().split()
    student_list.append([line[0], int(line[1]), int(line[2]), int(line[3])])
result = sorted(student_list, key = lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(len(result)):
    print(result[i][0])