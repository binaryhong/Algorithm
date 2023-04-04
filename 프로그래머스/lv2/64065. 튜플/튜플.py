def solution(s):
    answer = []
    s = s.replace("{", "[").replace("}", "]")
    s = s[1:-1].split("],[")
    result = []
    for item in s:
        item = item.replace("[", "").replace("]", "")
        result.append(list(map(int, item.split(","))))

    sortedResult = sorted(result,key=len)
    while sortedResult:
        value = sortedResult[0].pop(0)
        answer.append(value)
        sortedResult = [x for x in sortedResult if x]
        for x in sortedResult:
            x.remove(value)

    return answer