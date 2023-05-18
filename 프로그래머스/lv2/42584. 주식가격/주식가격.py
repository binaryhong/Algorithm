def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        second = 0
        for j in range(i,len(prices)-1):
                if prices[j] >= prices[i]:
                    second += 1
                else:
                    break
        answer.append(second)
    answer.append(0)
    return answer