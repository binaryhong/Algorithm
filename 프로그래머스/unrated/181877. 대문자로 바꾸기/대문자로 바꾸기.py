def solution(myString):
    answer = ""
    for i in range(len(myString)):
        if myString[i].lower():
            answer += myString[i].upper()
        else:
            answer += myString[i]
    return answer