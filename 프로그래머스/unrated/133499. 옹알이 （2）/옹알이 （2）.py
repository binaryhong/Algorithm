def solution(babbling):
    babble = ["", "aya", "ye", "woo", "ma"]
    cnt = 0
    for value in babbling:
        for babbleValues in babble:
            if babbleValues * 2 not in value:
                value = value.replace(babbleValues, " ")
        if value.strip() == "":
            cnt += 1
    return cnt