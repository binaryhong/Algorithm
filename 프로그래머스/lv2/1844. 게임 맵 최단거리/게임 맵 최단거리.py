from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque()
    queue.append((0, 0))
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    return visited[n-1][m-1]
