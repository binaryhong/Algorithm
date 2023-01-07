def solution(my_string):
    my_string += "A"
    n = len(my_string) 
    answer = 0
    tmp = 0
    for i in range(n):
        if my_string[i].isdigit():
            tmp = tmp*10 + int(my_string[i]) 
        else:
            answer += tmp 
            tmp = 0 
    return answer