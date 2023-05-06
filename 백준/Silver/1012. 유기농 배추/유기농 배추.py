from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0] # x축 이동을 위한 리스트
    dy = [0, 0, 1, -1] # y축 이동을 위한 리스트
    queue = deque() # 큐 생성
    queue.append((x,y)) # 시작 위치를 큐에 삽입
    while queue: # 큐가 빌 때까지 반복
        x,y = queue.popleft() # 큐에서 첫 번째 원소를 꺼냄
        for i in range(4): # 상하좌우로 이동
            nx = x + dx[i] # 다음 x좌표 계산
            ny = y + dy[i] # 다음 y좌표 계산
            if (0 <= nx < n) and (0 <= ny < m): # 다음 좌표가 그래프 범위 내에 있는 경우
                if graph[nx][ny] == 1: # 다음 좌표에 배추가 있는 경우
                    graph[nx][ny] = -1 # 방문 처리
                    queue.append((nx,ny)) # 큐에 삽입

t = int(input()) # 테스트 케이스 개수 입력
for _ in range(t): # 테스트 케이스 개수만큼 반복
    m,n,k = map(int,input().split()) # 가로길이 m, 세로길이 n, 배추 위치 개수 k 입력
    graph = [[0]*m for _ in range(n)] # 그래프 초기화
    cnt = 0 # 필요한 최소의 배추흰지렁이 마리 수 초기화
    for _ in range(k): # 배추 위치 개수만큼 반복
        a,b = map(int,input().split()) # 배추 위치 입력
        graph[b][a] = 1 # 그래프에 배추 위치 표시
    for i in range(n): # 전체 그래프 순회
        for j in range(m):
            if graph[i][j] > 0: # 방문하지 않은 배추가 있는 경우
                bfs(i,j) # bfs 함수 호출
                cnt += 1 # 카운트 증가
    print(cnt) # 필요한 최소의 배추흰지렁이 마리 수 출력