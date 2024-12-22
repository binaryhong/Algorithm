# 입력 변수 받기
N, M, V = map(int, input().split())

# 인접 영행렬 생성
matrix = [[0] * (N + 1) for i in range(N + 1)]

# 방문한 곳 체크를 위한 배열 선언
visited = [0] * (N + 1)  # [0, 0, 0, 0, 0]

# 입력 받는 두 값에 대해 영행렬에 1 삽입
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1  # 1->2 2<-1 모두 연결되어 있기 때문일까?
    # matrix 간선이 연결되어있으면 1로 값 변경.

def dfs(V):
    # 방문한 곳은 1 넣기
    visited[V] = 1

    print(V, end=' ')

    # 재귀 함수 선언(V와 인접한 곳을 찾고 방문하지 않았다면 함수 실행)
    for i in range(1, N + 1):
        if visited[i] == 0 and matrix[V][i] == 1:  #방문하지 않았고, 간선이 있는지.
            dfs(i)


visited_bfs = [0] * (N+1)
from collections import deque
def bfs(v):
    visited_bfs[v] = 1                         # 방문처리
    queue = deque()
    queue.append(v)                            # 큐에 노드 삽입
    while queue:                               # 큐에 노드가 없을때까지 반복
        node = queue.popleft()                 # 큐에서 빼주기
        print(node,end=' ')
        for i in range(N+1):
            if visited_bfs[i] == 0 and matrix[i][node]: # 방문했었는지, 그리고 간선이 있는지 확인
                queue.append(i)                        # 큐에 노드 삽입
                visited_bfs[i] = 1                     # 방문처리

dfs(V)
# dfs 를 완료한 visited 배열(1로 되어있음)에서 0으로 방문체크
print()
bfs(V)