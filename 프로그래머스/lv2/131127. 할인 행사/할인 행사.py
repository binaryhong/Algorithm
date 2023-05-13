def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    count = 0
    for i in range(len(discount)-9):
        temp_dict = want_dict.copy()
        for j in range(i, i+10):
            if discount[j] in temp_dict:
                temp_dict[discount[j]] -= 1
                if temp_dict[discount[j]] == 0:
                    del temp_dict[discount[j]]
        if not temp_dict:
            count += 1
    return count