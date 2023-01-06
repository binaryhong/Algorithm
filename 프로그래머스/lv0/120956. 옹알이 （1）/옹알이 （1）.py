def solution(babbling):
    have = "aya", "ye", "woo", "ma"
    have_list = []
    for i in range(len(have)):
        have_list.append(have[i])
    for i in range(len(have)):
        for j in range(len(have)):
            if i !=j:
                have_list.append(have[i]+have[j])
    for i in range(len(have)):
        for j in range(len(have)):
            for k in range(len(have)):
                if i != j and j != k and i != k:
                    have_list.append(have[i]+have[j]+have[k])
    for i in range(len(have)):
        for j in range(len(have)):
            for k in range(len(have)):
                for l in range(len(have)):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        have_list.append(have[i]+have[j]+have[k]+have[l])

    cnt = 0
    for i in range(len(babbling)):
        for j in range(len(have_list)):
            if babbling[i] == have_list[j]:
                cnt += 1
    return cnt