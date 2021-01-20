from collections import deque  # deque 라이브러리 사용 
n, m = map(int, input().split())

maze = []  # 미로

# 미로 입력 받음
for i in range(n):  
    maze.append(list(map(int, input())))

# 상하좌우 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue.append((x,y))
    while queue:  # 큐가 빌 때까지 반복
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 범위를 벗어나면 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 괴물이 있어서 못지나가는 곳도 무시
            if maze[nx][ny] == 0:
                continue
            # 처음 방문하는 노드에만 번호를 매김
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 # 움직인 칸마다 번호를 매김
                queue.append((nx,ny))
    return maze[n-1][m-1]  # 출구의 번호지만 번호가 답이 됨

print(bfs(0,0))












bfs(1,1)