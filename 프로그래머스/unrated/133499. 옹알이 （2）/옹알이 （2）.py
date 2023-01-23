def solution(babbling):

    word = ["aya", "ye", "woo", "ma"]
    result = 0

    for i in babbling:

        if len(i) < 2:
            pass

        else:
            while True:
                if i[:2] in word and i[:2] != i[2:4]:
                    i = i[2:]

                elif i[:3] in word and i[:3] != i[3:6]:
                    i = i[3:]

                elif i == '':
                    result += 1
                    break

                else:
                    break

    answer = result

    return answer