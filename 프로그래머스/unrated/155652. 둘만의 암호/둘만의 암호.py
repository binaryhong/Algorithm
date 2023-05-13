from string import ascii_lowercase
def solution(s, skip, index):
    alphabet_list = list(ascii_lowercase)
    for i in range(len(skip)):
        if skip[i] in alphabet_list:
            alphabet_list.pop(alphabet_list.index(skip[i]))
    answer = ""
    for i in range(len(s)):
        for j in range(len(alphabet_list)):
            if s[i] == alphabet_list[j]:
                answer += alphabet_list[(j+index) % len(alphabet_list)]
    return answer