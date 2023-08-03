cnt = 0
num = int(input())
for i in range(num):
    subject = list(map(float, input().split()))
    sumValue = sum(subject) - subject[0]
    averageValue = sumValue / subject[0]  # 학생 수인 subject[0]값으로 나눔.
    for j in range(1, len(subject)):
        if subject[j] > averageValue:
            cnt += 1
        else:
            pass
    answer = cnt / (len(subject) - 1) * 100  # len에서 -하는 이유 : 첫번째 받은 학생 수 삭제를 위함.
    print("%0.3f%%" % answer)
    cnt = 0