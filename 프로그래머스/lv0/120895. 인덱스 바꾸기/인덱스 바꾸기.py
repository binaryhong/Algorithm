def solution(my_string, num1, num2):
    answer = ''
    for i in range(0, num1):
        answer += my_string[i]
    answer += my_string[num2]
    for i in range(num1+1,len(my_string)):
        if i == num2:
            answer += my_string[num1]
        else:
            answer += my_string[i]
    return answer