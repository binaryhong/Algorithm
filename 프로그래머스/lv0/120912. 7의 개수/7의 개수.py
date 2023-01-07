def solution(array):
    answer = 0
    for i in range (0,len(array)):
        for c in str(array[i]):
            if c == "7":
                answer += 1

    return answer
