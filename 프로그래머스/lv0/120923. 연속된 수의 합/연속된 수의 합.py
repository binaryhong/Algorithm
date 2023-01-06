import math
def solution(num, total):
    result = []
    if num == 1:
        return [total]
    if num % 2 == 1:
        for i in range(total // num - (num - 1) // 2, total // num + (num - 1) // 2 + 1):
            result.append(i)
        return result
    else:
        for i in range(total // num - (num - 1) // 2, math.ceil(total // num) + (num - 1) // 2 + 2):
            result.append(i)
        return result
