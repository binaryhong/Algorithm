def solution(num_str):
    listA = []
    for i in range(len(num_str)):
        listA.append(int(num_str[i]))
    return sum(listA)