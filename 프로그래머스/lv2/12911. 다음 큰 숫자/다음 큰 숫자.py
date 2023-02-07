def solution(n):
    answer = n
    cnt = bin(n).count('1')

    while True:                             
        answer += 1
        answerCnt = bin(answer).count('1')
        if answerCnt == cnt:
            break
    return answer