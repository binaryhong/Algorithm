def solution(my_string, letter):
    a = list(my_string)
    for i in range(len(a)):
        if a[i] == letter:
            a[i] = ""
    return ''.join(a)