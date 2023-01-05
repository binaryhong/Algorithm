def solution(numbers, direction):
    result = []
    if direction == "right":
        result.append(numbers.pop())
        for i in range(len(numbers)):
            result.append(numbers[i])
    else:
        for i in range(1,len(numbers)):
            result.append(numbers[i])
        result.append(numbers[0])

    return result