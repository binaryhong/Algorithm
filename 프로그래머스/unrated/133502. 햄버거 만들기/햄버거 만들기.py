def solution(ingredient):
    answer = 0
    x = 0
    y = 0
    while x == 0:
        lenIngredient = len(ingredient)
        for i in range(y, len(ingredient)):
            if ingredient[i:i + 4] == [1, 2, 3, 1]:
                answer += 1
                del ingredient[i:i+4]
                y = i - 3
                break
        if i + 1 == lenIngredient:
            x = 2
    return answer