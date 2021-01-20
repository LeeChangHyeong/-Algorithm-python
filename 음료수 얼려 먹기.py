n, m = map(int, input().split())

ice_block = []   #  얼음판
for i in range(n):  # 얼음판 입력받기
    ice_block.append(list(map(int, input())))


def dfs(x, y):
    # 범위를 벗어나면 False를 반환
    if x <= -1 or x >=n or y <= -1 or y >= m: 
        return False
    # 내가 확인한 노드가 방문하지 않았던 노드였다면
    if ice_block[x][y] == 0:
        # 방문 처리
        ice_block[x][y] = 1
        # (순서대로)상,하,좌,우의 위치도 재귀 함수를 이용하여 구함
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0  # 아이스크림 갯수
for i in range(n):
    for j in range(m):
        if dfs(i ,j) == True:
            result = result + 1

print(result)