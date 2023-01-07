def solution(emergency):
    a = sorted(emergency, reverse=True)
    print("a:",a)
    answer = []
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if emergency[i] == a[j]:
                answer.append(j+1)
    return answer