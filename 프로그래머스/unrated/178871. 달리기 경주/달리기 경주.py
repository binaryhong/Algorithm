def solution(players, callings):
    playerDict = {value: index for index, value in enumerate(players)}

    for i in callings:
        if i in playerDict:
            index = playerDict[i]
            players[index], players[index - 1] = players[index - 1], players[index]
            playerDict[players[index]], playerDict[players[index - 1]] = playerDict[players[index - 1]], playerDict[players[index]]
    return players