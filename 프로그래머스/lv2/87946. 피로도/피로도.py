from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    for order in permutations(dungeons):
        fatigue = k
        count = 0
        for dungeon in order:
            if fatigue >= dungeon[0]:
                fatigue -= dungeon[1]
                count += 1
            else:
                break
        max_dungeons = max(max_dungeons, count)
    return max_dungeons