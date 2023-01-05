def solution(age):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ''
    for i in range(len(str(age))):
        value = age % 10
        answer += alpha[value]
        age = age // 10
    return answer[::-1]