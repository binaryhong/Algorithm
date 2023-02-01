def solution(lottos, win_nums):
    lottoCnt = 0
    for i in range(6):
        for j in range(6):
            if lottos[i] == win_nums[j]:
                lottoCnt += 1
                break
    
    answer = [0, 0]

    if lottoCnt == 6:
        answer[0] = 1
        answer[1] = 1
    elif lottoCnt == 5 and lottos.count(0) == 1:
        answer[0] = 1
        answer[1] = 2
    elif lottoCnt == 5 and lottos.count(0) == 0:
        answer[0] = 2
        answer[1] = 2
    elif lottoCnt == 4 and lottos.count(0) == 2:
        answer[0] = 1
        answer[1] = 3
    elif lottoCnt == 4 and lottos.count(0) == 1:
        answer[0] = 2
        answer[1] = 3
    elif lottoCnt == 4 and lottos.count(0) == 0:
        answer[0] = 3
        answer[1] = 3
    elif lottoCnt == 3 and lottos.count(0) == 3:
        answer[0] = 1
        answer[1] = 4
    elif lottoCnt == 3 and lottos.count(0) == 2:
        answer[0] = 2
        answer[1] = 4
    elif lottoCnt == 3 and lottos.count(0) == 1:
        answer[0] = 3
        answer[1] = 4
    elif lottoCnt == 3 and lottos.count(0) == 0:
        answer[0] = 4
        answer[1] = 4
    elif lottoCnt == 2 and lottos.count(0) == 4:
        answer[0] = 1
        answer[1] = 5
    elif lottoCnt == 2 and lottos.count(0) == 3:
        answer[0] = 2
        answer[1] = 5
    elif lottoCnt == 2 and lottos.count(0) == 2:
        answer[0] = 3
        answer[1] = 5
    elif lottoCnt == 2 and lottos.count(0) == 1:
        answer[0] = 4
        answer[1] = 5
    elif lottoCnt == 1 and lottos.count(0) == 5:
        answer[0] = 1
        answer[1] = 6
    elif lottoCnt == 1 and lottos.count(0) == 4:
        answer[0] = 2
        answer[1] = 6
    elif lottoCnt == 1 and lottos.count(0) == 3:
        answer[0] = 3
        answer[1] = 6
    elif lottoCnt == 1 and lottos.count(0) == 2:
        answer[0] = 4
        answer[1] = 6
    elif lottoCnt == 1 and lottos.count(0) == 1:
        answer[0] = 5
        answer[1] = 6
    elif lottoCnt == 1 and lottos.count(0) == 0:
        answer[0] = 6
        answer[1] = 6
    elif lottoCnt == 0 and lottos.count(0) == 6:
        answer[0] = 1
        answer[1] = 6
    elif lottoCnt == 0 and lottos.count(0) == 5:
        answer[0] = 2
        answer[1] = 6
    elif lottoCnt == 0 and lottos.count(0) == 4:
        answer[0] = 3
        answer[1] = 6
    elif lottoCnt == 0 and lottos.count(0) == 3:
        answer[0] = 4
        answer[1] = 6
    elif lottoCnt == 0 and lottos.count(0) == 2:
        answer[0] = 5
        answer[1] = 6
    elif lottoCnt == 0 and lottos.count(0) == 1:
        answer[0] = 6
        answer[1] = 6
    elif lottoCnt == 0 and lottos.count(0) == 0:
        answer[0] = 6
        answer[1] = 6

    return answer