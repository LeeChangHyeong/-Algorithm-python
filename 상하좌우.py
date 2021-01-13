n = int(input())
plans = input().split()

x, y = 1, 1 #시작 좌표겸 답이 될 좌표
dx = [0, 0, -1, 1] #U,D에 따른 이동 방향
dy = [-1, 1, 0, 0] #L,R에 따른 이동 방향
move = ['L', 'R', 'U', 'D'] #plans랑 비교하기 위해 만듬

for plan in plans: #plans에서 하나 하나 꺼냄
    #1)
    for i in range(len(move)):
        if plan == move[i]: #비교
            nx = x + dx[i] 
            ny = y + dy[i]
    #2)
    if nx < 1 or ny < 1 or ny > n or nx > n: #범위 밖을 나가버리면 무시
        continue
    #3)
    x, y = nx, ny
print(x,y)
    