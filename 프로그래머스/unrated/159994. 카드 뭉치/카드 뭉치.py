def solution(cards1, cards2, goal):
    i = j = k = 0
    while i < len(cards1) and j < len(cards2) and k < len(goal):
        if goal[k] == cards1[i]:
            i += 1
            k += 1
        elif goal[k] == cards2[j]:
            j += 1
            k += 1
        else:
            return "No"
    while i < len(cards1) and k < len(goal):
        if goal[k] == cards1[i]:
            i += 1
            k += 1
        else:
            return "No"
    while j < len(cards2) and k < len(goal):
        if goal[k] == cards2[j]:
            j += 1
            k += 1
        else:
            return "No"
    if k == len(goal):
        return "Yes"
    else:
        return "No"