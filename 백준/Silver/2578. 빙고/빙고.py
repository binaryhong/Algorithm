bingoCnt = 0
user_bingo = [list(map(int, input().split())) for _ in range(5)]
All_bingo = user_bingo[:]
appendList2 = []
appendList3 = []
for i in range(5):
    appendList = []
    for j in range(5):
        appendList.append(user_bingo[j][i])
        if i == j:
            appendList2.append(user_bingo[i][j])
        if i + j == 4:
            appendList3.append(user_bingo[i][j])
    All_bingo.append(appendList)
All_bingo.append(appendList2)
All_bingo.append(appendList3)
answer_bingo = []
jList = []
for i in range(5):
    line = map(int, input().split())
    answer_bingo.extend(line)
    for i in range(len(answer_bingo)):
        for j in range(len(All_bingo)):
            if answer_bingo[i] in All_bingo[j]:
                All_bingo[j][All_bingo[j].index(answer_bingo[i])] = 0
            if sum(All_bingo[j]) == 0 and j not in jList:
                jList.append(j)
                bingoCnt += 1
                if bingoCnt == 3:
                    print(i+1)
                    break
        if bingoCnt == 3:
            break