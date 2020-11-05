n = int(input())
s = 1
if n == 1: 
    print(1)
else:
    for i in range(n):
        s = s + 6*i #첫번째 1 빼고는 6씩 증가하는 규칙이기 때문에 1을 더해줌
        if s > n:
            print(i+1)
            break
