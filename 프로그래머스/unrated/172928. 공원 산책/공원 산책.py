def solution(park, routes):
    # 위치 index
    x = 0
    y = 0

    # 시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = j
                y = i
                break

    # 이동
    for route in routes:
        # 위치 초기화
        xx = x
        yy = y
        # 이동 - 장애물이 있거나 공원을 벗어나면 명령 무시
        direction, steps = route.split()
        steps = int(steps)
        for step in range(steps):
            # 동쪽 : 현재 위치가 map 가장 오른쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            if direction == 'E' and xx != len(park[0]) - 1 and park[yy][xx + 1] != 'X':
                xx += 1
                if step == steps - 1:
                    x = xx  # step만큼 움직였으면 위치 초기화
            # 서쪽 : 현재 위치가 map 가장 왼쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif direction == 'W' and xx != 0 and park[yy][xx - 1] != 'X':
                xx -= 1
                if step == steps - 1:
                    x = xx
            # 남쪽 : 현재 위치가 map 가장 아래쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif direction == 'S' and yy != len(park) - 1 and park[yy + 1][xx] != 'X':
                yy += 1
                if step == steps - 1:
                    y = yy
            # 북쪽 : 현재 위치가 map 가장 위쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif direction == 'N' and yy != 0 and park[yy - 1][xx] != 'X':
                yy -= 1
                if step == steps - 1:
                    y = yy

    return [y, x]