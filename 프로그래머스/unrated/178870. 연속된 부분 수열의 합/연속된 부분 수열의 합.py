def solution(sequence, k):
    answer = []
    n = len(sequence)
    left, right = 0, 0
    sumValue = sequence[0]
    while left <= right and right < n:
        if sumValue < k:
            right += 1
            if right < n:
                sumValue += sequence[right]
        elif sumValue > k:
            sumValue -= sequence[left]
            left += 1
        else:
            answer.append([left, right])
            sumValue -= sequence[left]
            left += 1
    if len(answer) == 0:
        return []
    else:
        min_diff = float('inf')
        min_index = -1
        for i in range(len(answer)):
            if answer[i][1] - answer[i][0] < min_diff:
                min_diff = answer[i][1] - answer[i][0]
                min_index = i
        return answer[min_index]