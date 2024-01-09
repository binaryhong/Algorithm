a=input()
def reverse_string(s):
    return s[::-1]

def process_string(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == '<':
            i += 1
            temp = ''
            while s[i] != '>':
                temp += s[i]
                i += 1
            i += 1
            result.append('<' + temp + '>')
        elif s[i].isspace():
            result.append(s[i])
            i += 1
        else:
            temp = ''
            while i < len(s) and not s[i].isspace() and s[i] != '<':
                temp += s[i]
                i += 1
            result.append(reverse_string(temp))
    return ''.join(result)
print(process_string(a))