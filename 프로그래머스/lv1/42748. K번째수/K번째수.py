def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        copyArray = array[commands[i][0]-1:commands[i][1]]
        copyArray.sort()
        answer.append(copyArray[commands[i][2]-1])
    return answer