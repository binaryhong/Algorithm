def solution(number, limit, power):
    cntList = [1]
    for i in range(2, number + 1):
        cnt = 0
        for j in range(1, int(i ** (1 / 2) + 1)):
            if i % j == 0:
                cnt += 1
                if j ** 2 != i:  # 제곱이 되는 약수 중복 방지
                    cnt += 1
        if cnt > limit:  # 소수의 개수가 limit를 넘어가면
            cntList.append(power)
        else:
            cntList.append(cnt)
    return sum(cntList)