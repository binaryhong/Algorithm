def solution(s):
    word = s.split(" ")
    print("word:", word)
    answer = ""
    for i in range(len(word)):
        for j in range(len(word[i])):
            if j % 2 == 0:
                answer += word[i][j].upper()
            if j % 2 == 1:
                answer += word[i][j].lower()
        answer += " "
    return answer[:-1]