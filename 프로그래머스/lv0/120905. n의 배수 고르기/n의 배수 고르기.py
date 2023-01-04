def solution(n, numlist):
    result = []
    for num in numlist:
        if num % n == 0:
            result.append(num)
    return result
