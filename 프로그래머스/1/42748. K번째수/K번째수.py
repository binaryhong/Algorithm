def solution(array, commands):
    commandsList = []
    answer = []
    for i in range(len(commands)):
        tempList = array[commands[i][0]-1 : commands[i][1]]
        tempList.sort()
        commandsList.append(tempList)
        # print("tempList[commands[i][2]]:",tempList[commands[i][2]])
        answer.append(tempList[commands[i][2]-1])
        # print("tempList:", tempList)
        # print("answer:", answer)
    return answer