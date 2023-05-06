from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())


def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 4칸이라 4이지 않을까.
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return


for i in range(n):
    cnt = 0
    n, m, K = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for j in range(K):
        X, Y = map(int, input().split())
        graph[X][Y] = 1  # 입력받은 좌표의 값을 1로 바꿔줌. 해당 좌표에 배추가 있음.
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:  # 1이면 bfs실행.
                bfs(graph, a, b)
                cnt += 1
    print(cnt)