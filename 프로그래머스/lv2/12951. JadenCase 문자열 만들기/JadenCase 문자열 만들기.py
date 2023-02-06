def solution(s):
    listS = list(s)
    for i in range(len(listS)):
        if listS[i].isupper():
            listS[i] = listS[i].lower()
    for i in range(len(listS)):
        try:
            if listS[i - 1] == " ":
                listS[i] = listS[i].upper()
        except:
            pass
    if listS[0].islower():
        listS[0] = listS[0].upper()
    return "".join(listS)