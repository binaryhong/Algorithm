def solution(num_list, n):
    answer = []
    result = []
    for i in range(0,len(num_list)):
        for j in range(i+n-1,len(num_list)):
            answer.append(num_list[i:i+n])
            break
    for i in range(0,len(num_list), n):
        for j in range(n):
            result.append(answer[i])
            break
    return result