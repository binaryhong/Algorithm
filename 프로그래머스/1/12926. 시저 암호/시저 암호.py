def solution(s, n):
    from string import ascii_lowercase,ascii_uppercase
    upperList = [char for char in ascii_uppercase]
    lowerList = [char for char in ascii_lowercase]
    answer = ''
    for value in s:
        if value == " ":
            answer += " "
        if value in upperList:
            upperListIndex = (upperList.index(value) + n) % 26
            answer += upperList[upperListIndex]
        if value in lowerList:
            lowerListIndex = (lowerList.index(value) + n) % 26
            answer += lowerList[lowerListIndex]
    return answer