def solution(num_list):
    a = 1
    if(len(num_list)) >=11:
        return sum(num_list)
    else:
        for i in range(len(num_list)):
            a *= num_list[i]
        return a
