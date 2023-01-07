def solution(s):
    answer = ""
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            answer += s[i]
    return "".join(sorted(list(answer)))