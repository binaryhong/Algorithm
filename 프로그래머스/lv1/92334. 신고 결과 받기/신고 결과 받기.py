def solution(id_list, report, k):
    reportedCntDict = {i: 0 for i in id_list}
    reportedDict = {i: [] for i in id_list}
    list_report = list(set(report))
    for value in list_report:
        split_value = value.split()
        if split_value[1] in reportedCntDict:
            reportedCntDict[split_value[1]] += 1
            reportedDict[split_value[0]].append(split_value[1])
    answer = []
    for key in id_list:
        cnt = 0
        for value in reportedDict[key]:
            if reportedCntDict[value] >= k:
                cnt += 1
        answer.append(cnt)
    return answer