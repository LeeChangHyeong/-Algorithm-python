n = int(input())

# d[1]은 가로의 길이가 1일 때 채울 수 있는 경우의 수를 뜻함
d = [0]*1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]*2) % 796796

print(d[n])