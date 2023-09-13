aList = []
nSelfNumber = []
for i in range(1, 10001):
    aList.append(i)
    if 0 < i < 10:
        nSelfNumber.append(i + (i % 10))
    elif 10 <= i < 100:
        nSelfNumber.append(i + (i // 10) + (i % 10))
    elif 100 <= i < 1000:
        nSelfNumber.append(i + (i // 100) + ((i // 10) - i // 100 * 10) + (i % 10))
    elif 1000 <= i < 10000:
        nSelfNumber.append(i + (i // 1000) + (i // 100 - i // 1000 * 10) + (i // 10 - i // 100 * 10) + (i % 10))
    elif i == 10000:
        nSelfNumber.append(i + (i // 10000) + (i // 1000) + (i // 100) + (i // 10) + (i % 10))
    else:
        pass
result = sorted(list(set(aList) - set(nSelfNumber)))
for results in result:
    print(results)