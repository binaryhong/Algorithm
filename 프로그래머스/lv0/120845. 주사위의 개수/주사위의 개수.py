def solution(box, n):
    answer = []
    box.sort(reverse=True)
    for i in range(len(box)):
        answer.append(box[i] // n)
    final = 1
    for value in answer:
        final *= value
    return final