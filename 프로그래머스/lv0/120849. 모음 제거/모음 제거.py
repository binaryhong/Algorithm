def solution(my_string):
    for i in range(len(my_string)):
        my_string = my_string.replace("a","")
        my_string = my_string.replace("e","")
        my_string = my_string.replace("i","")
        my_string = my_string.replace("o","")
        my_string = my_string.replace("u","")
    return my_string