def solution(my_string):
    result = ""
    for i in range(len(my_string)):
        if my_string[i].isupper():
            result += my_string[i].lower()
        elif my_string[i].islower():
            result +=  my_string[i].upper()
    return result