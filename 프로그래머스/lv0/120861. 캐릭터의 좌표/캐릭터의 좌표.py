def solution(keyinput, board):
    result = [0,0]
    for i in range(len(keyinput)):
        if keyinput[i] == "left":
            result[0] -= 1
            if result[0] < (board[0]-1)//2 * (-1):
                result[0] += 1
        elif keyinput[i] == "right":
            result[0] += 1
            if result[0] > (board[0]-1)//2:
                result[0] -= 1
        elif keyinput[i] == "down":
            result[1] -= 1
            if result[1] < (board[1]-1)//2 * (-1):
                result[1] += 1
        elif keyinput[i] == "up":
            result[1] += 1
            if result[1] > (board[1]-1)//2:
                result[1] -= 1

    return result