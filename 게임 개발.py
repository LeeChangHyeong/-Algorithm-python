n, m = map(int, input().split())
x, y , look = map(int, input().split())
d = [[0] * m for _ in range(n)]  # 가본 곳인지 안가본곳인지 기록하기 위해 맵을 따로 0으로 초기화(중요)

maps = []  
for i in range(n):
    maps.append(list(map(int, input().split())))  # 맵을 입력받음

#  북 동 남 서(순서대로) 이동 좌표
dx = [-1,0,1,0] 
dy = [0,1,0,-1]

#  문제에 맞게 왼쪽으로 캐릭터를 돌리는 함수 생성
def turn_left():
    global look 
    look = look - 1  # 문제에서 북:0 동:1 남:2 서:3 이 주어졌기 때문에 -1을 해주면 왼쪽으로 90도 회전이 된다.
    if look == -1:  # 북쪽(0)에서 -1을 하면 -1이 되기때문에 -1은 3으로 바꿔준다.
        look = 3

turn_time = 0  # 캐릭터가 회전한 횟수를 기록(중요함) - 동서남북을 다 돌았는지 확인하기 위해
count = 1  # 캐릭터가 방문한 칸 횟수

# 시뮬레이션 시작
while True:
    turn_left()  # 왼쪽으로 돌린 후
    nx = x + dx[look]  # nx에 x좌표가 이동한걸 저장
    ny = y + dy[look]  # ny에 y좌표가 이동한걸 저장

    if d[nx][ny] == 0 and maps[nx][ny] == 0:  # d에선 0이 탐험하지 않은 곳 maps에선 0이 육지(갈수있는 곳)
        x = nx
        y = ny
        count = count + 1  # 한칸을 더 방문 했으니 count에 +1
    else:  # 방문을 한 곳이거나 바다이면
        turn_time += 1  # turn_time을 증가 시켜준다.
    if turn_time == 4:  # turn_time이 4가 되면(동,서,남,북 4방향을 다 확인해도 갈 곳이 없다는 뜻)
        # 뒤로 돌아감
        nx = x - dx[look]  
        ny = y - dy[look]
        # 뒤가 바다면 종료
        if maps[nx][ny] == 1:
            break
        # 뒤가 바다가 아니면
        else:
            x = nx
            y = ny
        turn_time = 0  # 0으로 초기화 시킨후 while문 반복

print(count)

