def solution(my_string):
    answer = []
    listA = []
    for i in range(len(my_string)):
        listA.append(my_string[i])
    for x in listA:
        if x not in answer:
            answer.append(x)

    return ''.join(answer)