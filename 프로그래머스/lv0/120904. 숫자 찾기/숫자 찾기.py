def solution(num, k):
    listA = []
    for i in range(len(str(num))):
        listA.append(int(str(num)[i]))
    if k in listA:
        return listA.index(k) + 1
    else:
        return -1