def solution(quiz):
    new_quiz = []
    answer = []
    for i in range(0,len(quiz)):
        new_quiz.append(quiz[i].split())
    for i in range(0,len(new_quiz)):
        for j in range(len(new_quiz[i])):
            if new_quiz[i][j] == "+":
                if int(new_quiz[i][0])+int(new_quiz[i][2]) == int(new_quiz[i][4]):
                    answer.append("O")
                else:
                    answer.append("X")
            if new_quiz[i][j] == "-":
                if int(new_quiz[i][0])-int(new_quiz[i][2]) == int(new_quiz[i][4]):
                    answer.append("O")
                else:
                    answer.append("X")
    return answer