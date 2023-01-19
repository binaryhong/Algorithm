def solution(food):
    answer = ""
    for i in range(1, len(food)):
        if food[i] % 2 == 1:
            answer += str(i) * ((food[i] - 1) // 2)
        elif food[i] % 2 == 0:
            answer += str(i) * (food[i] // 2)
    return answer+"0"+answer[::-1]