c = int(input()) # 컴퓨터의 수
n = int(input()) # 네트워크 상에서 직ㅈ버 연결되어 있는 컴퓨터 쌍의 수
matrix = [[0] * (c + 1) for i in range(c + 1)]
for i in range(n):
    a,b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visited = [0] * (c + 1)
def dfs(v):
    visited[v] = 1
    #print("visited:",visited)
    for j in range(c+1):
        if visited[j] == 0 and matrix[v][j] ==1:  #방문하지 않았고, 간선이 있는지.
            dfs(j)
    return sum(visited)-1
print(dfs(1))