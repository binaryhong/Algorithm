def solution(hp):
    j = hp // 5 # 장군
    hp = hp - j*5
    b = hp // 3 # 병정
    hp = hp - b*3
    return j+b+hp