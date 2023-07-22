def solution(storey):
    cnt = 0
    while storey > 0:
        value = 0
        # print("처음 storey:", storey)
        # if storey // 10 >= 5:
        #     storey += 100 - storey // 10
        # if storey // 10 < 5:
        #     storey -= 100 - storey // 10
        if storey % 10 > 5:
            cnt += 10 - storey % 10
            # print("cnt:", cnt)
            storey += 10 - storey % 10
            # print("중간 storey:", storey)
        if storey % 10 == 5:
            if (storey // 10) % 10 >= 5:
                cnt += 10 - storey % 10
                value = 10 - storey % 10
                storey += value
            elif (storey // 10) % 10 < 5:
                cnt += 10 - storey % 10
                storey -= 10 - storey % 10
        if storey % 10 < 5:
            cnt += storey % 10
            # storey += 10 - storey % 10
        # print("몫:", storey //10)
        storey = storey // 10
    return cnt