def solution(keymap, targets):
    result = []
    for target in targets:
        sumValue = 0
        for char in target:
            indices = []
            for s in keymap:
                if char in s:
                    indices.append(s.index(char))
            if indices:
                min_index = min(indices)
                sumValue += min_index + 1
            else:
                sumValue = -1
                break
        result.append(sumValue)
    return result