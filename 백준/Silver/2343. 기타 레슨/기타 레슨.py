def solution(N, M, lessons):
    start = max(lessons)
    end = sum(lessons)

    while start <= end:
        mid = (start + end) // 2
        count = 1
        temp_sum = 0

        for lesson in lessons:
            if temp_sum + lesson > mid:
                temp_sum = lesson
                count += 1
            else:
                temp_sum += lesson

        if count <= M: 
            end = mid - 1
        else: 
            start = mid + 1

    return start


N, M = map(int,input().split())
lessons=list(map(int,input().split()))
print(solution(N ,M ,lessons))