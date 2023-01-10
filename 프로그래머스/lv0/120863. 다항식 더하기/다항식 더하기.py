def solution(polynomial):
    new_string = polynomial.split()
    strAnswer = 0 # 변수값 저장하기 위한곳.
    answer = 0 # 변수
    numberAnswer = 0 # 상수
    for i in range(len(new_string)):
        for j in range(len(new_string[i])):
            if new_string[i][-1] == "x":
                if new_string[i][j].isdigit():
                    strAnswer = strAnswer * 10 + int(new_string[i][j])
                elif len(new_string[i]) == 1:
                    answer += 1
                else:
                    answer += strAnswer
                    strAnswer = 0
            elif new_string[i][-1] != "x" and new_string[i][-1] != "+":
                numberAnswer += int(new_string[i])
                break


    if numberAnswer == 0 and answer == 1:
        return "x"
    elif numberAnswer == 0 and answer > 0:
        return str(answer) + "x"
    elif numberAnswer >0 and answer == 1:
        return "x" + " + " + str(numberAnswer)
    elif answer == 0:
        return str(numberAnswer)
    else:
        return str(answer) + "x" + " + " + str(numberAnswer)