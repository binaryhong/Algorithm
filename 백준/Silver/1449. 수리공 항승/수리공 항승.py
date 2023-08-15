N, L = map(int, input().split())  # N: 테이프의 길이, L: 테이프의 개수
location = list(map(int, input().split()))
location.sort()

# 테이프를 처음 붙이는 시작지점
start = location[0]
# 필요한 테이프의 개수
count = 1

# 물이 새는 곳의 위치를 차례대로 받으면서
for location in location[1:]:
    # 테이프를 붙이는 범위 내에 물이 새는 곳의 위치가 있다면
    if location in range(start, start + L):
        # 기존 테이프 사용
        continue
    # 기존의 테이프로 붙이지 못한다면
    else:
        # 새 테이프를 사용하고 테이프 개수 추가
        start = location
        count += 1

# 필요한 테이프의 개수 출력
print(count)