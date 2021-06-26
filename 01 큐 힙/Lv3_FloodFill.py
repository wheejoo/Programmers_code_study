from collections import deque
def solution(n, m, image):
    answer = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                answer += 1
                bfs(n,m,i,j,image,visited)
    return answer

def bfs(n,m,i,j,image,visited):
    q = deque()
    q.append((i,j))
    
    while q:
        x,y = q.popleft()
        visited[x][y] = True
        
        DELTAS = ((0,1),(0,-1),(1,0),(-1,0))
        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            
            if not (0<=nx<n and 0<=ny<m and not visited[nx][ny]):
                continue
                
            if image[nx][ny] == image[x][y]:
                q.append((nx,ny))
                visited[nx][ny] = True
