start_data = input()

row = int(start_data[1])  # x좌표
col = int(ord(start_data[0])) - int(ord('a')) + 1  # y좌표

count = 0
moves = [(-2,1),(-2,-1),(1,2),(-1,2),(2,1),(2,-1),(1,-2),(-1,-2)]  # 움직일 수 있는 모든 범위


for i in range(len(moves)):  # moves의 첫 번째 원소
    for j in range(1):  # moves의 첫 번째 원소 중 첫 원소 ex) moves[0][1] = (-2, 1) 중 1
        next_r = row + moves[i][j]  # 움직인 후 x 좌표
        next_c = col + moves[i][j+1]  # 움직인 후 y 좌표
        if next_r >= 1 and next_r <= 8 and next_c >= 1 and next_c <= 8:  # 움직인 좌표가 정원 밖을 나갔는지 검토 
            count = count + 1  # 안나갔으면 count에 1을 더해줌
print(count)
