def solution(s):
    answer = ""
    aDict = {"one": 1,
             "two": 2,
             "three": 3,
             "four": 4,
             "five": 5,
             "six": 6,
             "seven": 7,
             "eight": 8,
             "nine": 9,
             "zero": 0}
    value = ""
    for i in range(len(s)):
        value += s[i]
        if value in aDict.keys():
            answer += str(aDict[value])
            value = ""
        if value.isdigit():
            answer += value
            value = ""
    return int(answer)