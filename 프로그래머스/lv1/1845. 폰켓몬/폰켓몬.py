def solution(nums):
    choice_cnt = int(len(nums)//2)
    kind_cnt = len(set(nums))

    if choice_cnt > kind_cnt:
        return kind_cnt
    else:
        return choice_cnt