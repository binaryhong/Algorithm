def solution(new_id):
    # 1단계
    tempValue = ""
    new_id = new_id.lower()
    for index, value in enumerate(new_id):
        # 2단계
        if value.isalpha() or value.isdigit() or value == "-" or value == "_" or value ==".":
            tempValue += value
        new_id = tempValue
        # 3단계
        while ".." in new_id:
            new_id = new_id.replace("..",".")
        # print("3단계 이후 answer:", answer)

    # 4단계
        while new_id.startswith(".") or new_id.endswith("."):
            if new_id.startswith("."):
                new_id = new_id[1:]
            if new_id.endswith("."):
                new_id = new_id[:-1]
    # 5단계
        if not new_id:
            new_id += "a"
        #
    # 6단계
        if len(new_id) >= 16:
            new_id = new_id[:15]
            if new_id[-1] == ".":
                new_id = new_id[:-1]
    # 7단계
        if len(new_id) <= 2:
            while len(new_id) <=2:
                new_id += new_id[-1]
    return new_id