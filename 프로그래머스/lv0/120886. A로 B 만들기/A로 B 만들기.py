def solution(before, after):
    if list(sorted(list(before))) == list(sorted(list(after))):
        return 1
    else:
        return 0
