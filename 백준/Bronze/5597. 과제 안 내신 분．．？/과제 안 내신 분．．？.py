result = []
answer = []
for i in range(28):
    result.append(int(input()))
result.sort()

for i in range(1 ,len(result)):
    if result[i]-result[i-1] != 1:
        answer.append(result[i]-1)
if answer:
    answer.sort()
elif 1 and 30 not in answer:
    answer.append(1)
    answer.append(30)
elif 1 and 2 not in answer:
    answer.append(1)
    answer.append(2)
elif 29 and 30 not in answer:
    answer.append(29)
    answer.append(30)
for value in answer:
    print(value)