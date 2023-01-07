def solution(numbers):
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = ""
    result = ""
    for i in range(len(numbers)):
        answer += numbers[i]
        if answer in alpha:
            result += str(alpha.index(answer))
            answer = ""
    return int(result)