def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1 
    
    #  포인터 2개로 잡고 조건을 체크.
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1

        answer += 1
    return answer