def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        print("i:",i, "c:", c)
        if i + 1 > c:
            return i
    return len(citations)